variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "Kubernetes cluster name"
  type        = string
  default     = "salesgenie-platform"
}

variable "postgres_password" {
  description = "PostgreSQL admin password"
  type        = string
  sensitive   = true
}

variable "redis_password" {
  description = "Redis authentication password"
  type        = string
  sensitive   = true
}

variable "gcs_bucket_name" {
  description = "Google Cloud Storage bucket for files"
  type        = string
  default     = "salesgenie-documents"
}

variable "k8s_namespace" {
  description = "Kubernetes namespace"
  type        = string
  default     = "salesgenie"
}

variable "domain_name" {
  description = "Platform domain name"
  type        = string
  default     = "salesgenie.ai"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "production"
}

variable "instance_count" {
  description = "Number of service instances"
  type        = number
  default     = 3
}

variable "cpu_request" {
  description = "CPU request per container"
  type        = string
  default     = "500m"
}

variable "memory_request" {
  description = "Memory request per container"
  type        = string
  default     = "512Mi"
}

variable "cpu_limit" {
  description = "CPU limit per container"
  type        = string
  default     = "1000m"
}

variable "memory_limit" {
  description = "Memory limit per container"
  type        = string
  default     = "1Gi"
}