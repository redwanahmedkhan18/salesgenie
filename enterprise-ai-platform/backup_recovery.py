#!/usr/bin/env python3
"""
SalesGenie Backup & Disaster Recovery System
Provides automated backups, recovery procedures, and data protection
"""

import os
import subprocess
import shutil
import json
import logging
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import hashlib
import schedule
import time
import threading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("salesgenie.backup")

class BackupManager:
    def __init__(self):
        self.backup_dirs = [
            "/home/user/salesgenie/data",
            "/home/user/salesgenie/models",
            "/home/user/salesgenie/embeddings",
            "/home/user/salesgenie/config",
        ]
        self.backup_output = "/var/backups/salesgenie"
        self.retention_days = 30
        self.encryption_enabled = True
        self.gpg_key = os.getenv("BACKUP_GPG_KEY", "")
    
    def create_backup(self, backup_type: str = "full") -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"salesgenie_{backup_type}_{timestamp}"
        backup_path = os.path.join(self.backup_output, backup_name)
        
        os.makedirs(backup_path, exist_ok=True)
        
        for backup_dir in self.backup_dirs:
            if os.path.exists(backup_dir):
                dest = os.path.join(backup_path, os.path.basename(backup_dir))
                try:
                    shutil.copytree(backup_dir, dest, dirs_exist_ok=True)
                    logger.info(f"Backed up: {backup_dir}")
                except Exception as e:
                    logger.error(f"Failed to backup {backup_dir}: {e}")
        
        metadata = {
            "backup_name": backup_name,
            "type": backup_type,
            "timestamp": datetime.now().isoformat(),
            "size_bytes": self._get_dir_size(backup_path),
            "checksum": self._compute_checksum(backup_path),
            "files_count": self._count_files(backup_path)
        }
        
        with open(os.path.join(backup_path, "metadata.json"), "w") as f:
            json.dump(metadata, f, indent=2)
        
        if self.encryption_enabled and self.gpg_key:
            self._encrypt_backup(backup_path)
        
        logger.info(f"Backup completed: {backup_name}")
        return backup_path
    
    def _get_dir_size(self, path: str) -> int:
        total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total += os.path.getsize(fp)
        return total
    
    def _compute_checksum(self, path: str) -> str:
        hasher = hashlib.sha256()
        for dirpath, dirnames, filenames in os.walk(path):
            for f in sorted(filenames):
                fp = os.path.join(dirpath, f)
                with open(fp, 'rb') as file:
                    hasher.update(file.read())
        return hasher.hexdigest()
    
    def _count_files(self, path: str) -> int:
        count = 0
        for dirpath, dirnames, filenames in os.walk(path):
            count += len(filenames)
        return count
    
    def _encrypt_backup(self, backup_path: str):
        try:
            zip_path = backup_path + ".tar.gz"
            subprocess.run(
                ["tar", "-czf", zip_path, "-C", os.path.dirname(backup_path), 
                 os.path.basename(backup_path)],
                check=True, capture_output=True
            )
            
            encrypted_path = zip_path + ".gpg"
            subprocess.run(
                ["gpg", "--encrypt", "--recipient", self.gpg_key, "-o", encrypted_path, zip_path],
                check=True, capture_output=True
            )
            
            shutil.rmtree(backup_path)
            os.remove(zip_path)
            logger.info(f"Backup encrypted: {encrypted_path}")
        except Exception as e:
            logger.error(f"Encryption failed: {e}")
    
    def cleanup_old_backups(self):
        if not os.path.exists(self.backup_output):
            return
        
        cutoff = datetime.now() - timedelta(days=self.retention_days)
        for item in os.listdir(self.backup_output):
            item_path = os.path.join(self.backup_output, item)
            if os.path.isdir(item_path):
                mtime = datetime.fromtimestamp(os.path.getmtime(item_path))
                if mtime < cutoff:
                    shutil.rmtree(item_path)
                    logger.info(f"Removed old backup: {item}")

class DisasterRecovery:
    def __init__(self):
        self.backups = "/var/backups/salesgenie"
        self.restore_log = "/var/log/salesgenie/restore.log"
    
    def restore_from_backup(self, backup_name: str, target_dir: str = "/home/user/salesgenie/data") -> bool:
        backup_path = os.path.join(self.backups, backup_name)
        
        if not os.path.exists(backup_path):
            logger.error(f"Backup not found: {backup_name}")
            return False
        
        try:
            with open(os.path.join(backup_path, "metadata.json"), "r") as f:
                metadata = json.load(f)
            logger.info(f"Restoring backup: {metadata['backup_name']}")
            
            if os.path.exists(target_dir):
                shutil.rmtree(target_dir)
            
            for item in os.listdir(backup_path):
                src = os.path.join(backup_path, item)
                dst = os.path.join(target_dir, item)
                if os.path.isdir(src):
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)
            
            logger.info(f"Restore completed: {backup_name}")
            with open(self.restore_log, "a") as f:
                f.write(json.dumps({
                    "timestamp": datetime.now().isoformat(),
                    "backup": backup_name,
                    "target": target_dir,
                    "success": True
                }) + "\n")
            
            return True
        except Exception as e:
            logger.error(f"Restore failed: {e}")
            return False
    
    def verify_backup_integrity(self, backup_name: str) -> bool:
        backup_path = os.path.join(self.backups, backup_name)
        metadata_path = os.path.join(backup_path, "metadata.json")
        
        if not os.path.exists(metadata_path):
            return False
        
        with open(metadata_path, "r") as f:
            metadata = json.load(f)
        
        current_checksum = self._compute_checksum(backup_path)
        return current_checksum == metadata["checksum"]
    
    def _compute_checksum(self, path: str) -> str:
        hasher = hashlib.sha256()
        for dirpath, dirnames, filenames in os.walk(path):
            for f in sorted(filenames):
                fp = os.path.join(dirpath, f)
                with open(fp, 'rb') as file:
                    hasher.update(file.read())
        return hasher.hexdigest()

class ScheduledBackup:
    def __init__(self):
        self.backup_manager = BackupManager()
        self.disaster_recovery = DisasterRecovery()
    
    def start_scheduler(self):
        schedule.every().day.at("02:00").do(self.full_backup)
        schedule.every().hour.do(self.incremental_backup)
        schedule.every().day.at("03:00").do(self.cleanup_old_backups)
        schedule.every().sunday.at("04:00").do(self.verify_all_backups)
        
        thread = threading.Thread(target=self._run_scheduler, daemon=True)
        thread.start()
        logger.info("Backup scheduler started")
    
    def _run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(60)
    
    def full_backup(self):
        logger.info("Running full backup...")
        return self.backup_manager.create_backup("full")
    
    def incremental_backup(self):
        logger.info("Running incremental backup...")
        return self.backup_manager.create_backup("incremental")
    
    def cleanup_old_backups(self):
        self.backup_manager.cleanup_old_backups()
    
    def verify_all_backups(self):
        logger.info("Verifying all backups...")
        for item in os.listdir(self.backup_manager.backup_output):
            item_path = os.path.join(self.backup_manager.backup_output, item)
            if os.path.isdir(item_path) and item.startswith("salesgenie_"):
                if self.disaster_recovery.verify_backup_integrity(item):
                    logger.info(f"Backup verified: {item}")
                else:
                    logger.warning(f"Backup verification failed: {item}")

if __name__ == "__main__":
    backup_system = ScheduledBackup()
    backup_system.start_scheduler()
    
    print("Backup & Disaster Recovery System initialized")
    print("Scheduled:")
    print("  - Full backup: Daily at 02:00")
    print("  - Incremental backup: Every hour")
    print("  - Cleanup: Daily at 03:00")
    print("  - Verification: Weekly on Sunday at 04:00")