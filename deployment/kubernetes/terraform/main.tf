terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    azure = {
      source  = "hashicorp/azure"
      version = "~> 3.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "EKS cluster name"
  default     = "salesgenie-platform"
}

variable "postgres_password" {
  description = "PostgreSQL admin password"
  type        = string
  sensitive   = true
}

variable "redis_password" {
  description = "Redis password"
  type        = string
  sensitive   = true
}

variable "gcs_bucket_name" {
  description = "Google Cloud Storage bucket name"
  type        = string
}

variable "k8s_namespace" {
  description = "Kubernetes namespace for SalesGenie"
  default     = "salesgenie"
}

# VPC and Networking
resource "aws_vpc" "salesgenie" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "salesgenie-vpc"
  }
}

resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.salesgenie.id
  cidr_block        = "10.0.${count.index + 1}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  tags = {
    Name = "salesgenie-public-${count.index}"
  }
}

resource "aws_subnet" "private" {
  count             = 2
  vpc_id            = aws_vpc.salesgenie.id
  cidr_block        = "10.0.${count.index + 10}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  tags = {
    Name = "salesgenie-private-${count.index}"
  }
}

data "aws_availability_zones" "available" {}

# RDS PostgreSQL
resource "aws_db_instance" "salesgenie_postgres" {
  identifier          = "salesgenie-postgres"
  engine              = "postgres"
  engine_version      = "15.4"
  instance_class      = "db.t3.medium"
  allocated_storage   = 100
  storage_encrypted   = true
  username            = "postgres"
  password            = var.postgres_password
  db_subnet_group_name = aws_db_subnet_group.salesgenie.name
  vpc_security_group_ids = [aws_security_group.rds.id]
  
  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "sun:04:00-sun:05:00"
  
  enabled_cloudwatch_logs_exports = ["postgresql"]
  
  multi_az            = true
  publicly_accessible = false
  
  tags = {
    Name = "salesgenie-postgres"
  }
}

# ElastiCache Redis
resource "aws_elasticache_cluster" "salesgenie_redis" {
  cluster_id           = "salesgenie-redis"
  engine               = "redis"
  node_type            = "cache.t3.medium"
  num_cache_nodes      = 2
  parameter_group_name = "default.redis7"
  port                 = 6379
  
  subnet_group_name = aws_elasticache_subnet_group.salesgenie.name
  security_group_ids = [aws_security_group.redis.id]
  
  transit_encryption_enabled = true
  
  tags = {
    Name = "salesgenie-redis"
  }
}

# EKS Cluster
resource "aws_eks_cluster" "salesgenie" {
  name     = var.cluster_name
  role_arn = aws_iam_role.cluster.arn
  version  = "1.30"
  
  vpc_config {
    subnet_ids = aws_subnet.private[*].id
    security_group_ids = [aws_security_group.eks_cluster.id]
  }
  
  depends_on = [
    aws_iam_role_policy_attachment.cluster_AmazonEKSClusterPolicy,
  ]
}

# EKS Node Group
resource "aws_eks_node_group" "salesgenie_nodes" {
  cluster_name    = aws_eks_cluster.salesgenie.name
  node_group_name = "salesgenie-nodes"
  node_role_arn   = aws_iam_role.nodes.arn
  subnet_ids      = aws_subnet.private[*].id
  
  scaling_config {
    desired_size = 3
    max_size     = 10
    min_size     = 1
  }
  
  instance_types = ["t3.large", "t3.xlarge"]
  
  labels = {
    environment = "production"
  }
  
  tags = {
    Name = "salesgenie-nodes"
  }
}

# S3 Bucket for documents
resource "aws_s3_bucket" "salesgenie_documents" {
  bucket = "salesgenie-documents-${var.cluster_name}"
  
  tags = {
    Name = "salesgenie-documents"
  }
}

resource "aws_s3_bucket_versioning" "salesgenie_documents" {
  bucket = aws_s3_bucket.salesgenie_documents.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "salesgenie_documents" {
  bucket = aws_s3_bucket.salesgenie_documents.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# RDS Subnet Group
resource "aws_db_subnet_group" "salesgenie" {
  name       = "salesgenie-db-subnet-group"
  subnet_ids = aws_subnet.private[*].id
  
  tags = {
    Name = "salesgenie-db-subnet-group"
  }
}

# ElastiCache Subnet Group
resource "aws_elasticache_subnet_group" "salesgenie" {
  name       = "salesgenie-cache-subnet-group"
  subnet_ids = aws_subnet.private[*].id
}

# Security Groups
resource "aws_security_group" "rds" {
  name        = "salesgenie-rds-sg"
  description = "Security group for RDS"
  vpc_id      = aws_vpc.salesgenie.id
  
  ingress {
    description = "PostgreSQL"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    security_groups = [aws_security_group.eks_nodes.id]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "redis" {
  name        = "salesgenie-redis-sg"
  description = "Security group for Redis"
  vpc_id      = aws_vpc.salesgenie.id
  
  ingress {
    description = "Redis"
    from_port   = 6379
    to_port     = 6379
    protocol    = "tcp"
    security_groups = [aws_security_group.eks_nodes.id]
  }
}

resource "aws_security_group" "eks_cluster" {
  name        = "salesgenie-eks-cluster-sg"
  description = "Security group for EKS cluster"
  vpc_id      = aws_vpc.salesgenie.id
  
  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "eks_nodes" {
  name        = "salesgenie-eks-nodes-sg"
  description = "Security group for EKS nodes"
  vpc_id      = aws_vpc.salesgenie.id
}

# IAM Roles
resource "aws_iam_role" "cluster" {
  name = "salesgenie-eks-cluster-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "eks.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "cluster_AmazonEKSClusterPolicy" {
  role       = aws_iam_role.cluster.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
}

resource "aws_iam_role" "nodes" {
  name = "salesgenie-eks-nodes-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "nodes_AmazonEKSWorkerNodePolicy" {
  role       = aws_iam_role.nodes.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
}

# Outputs
output "cluster_endpoint" {
  value = aws_eks_cluster.salesgenie.endpoint
}

output "cluster_name" {
  value = aws_eks_cluster.salesgenie.name
}

output "postgres_endpoint" {
  value = aws_db_instance.salesgenie_postgres.endpoint
}

output "redis_endpoint" {
  value = aws_elasticache_cluster.salesgenie_redis.configuration_endpoint
}

output "s3_bucket" {
  value = aws_s3_bucket.salesgenie_documents.bucket
}