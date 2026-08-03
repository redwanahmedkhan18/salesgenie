#!/usr/bin/env python3
"""
SalesGenie Database Migration Manager
Run and manage PostgreSQL database migrations using Alembic-style migrations
"""

import os
import sys
import re
import json
import logging
from datetime import datetime
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass
import subprocess
import importlib.util

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("salesgenie.db-migration")

MIGRATIONS_DIR = "/home/user/salesgenie/enterprise-ai-platform/database/migrations"
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://salesgenie:password@localhost/salesgenie")

@dataclass
class Migration:
    revision: str
    down_revision: Optional[str]
    path: str
    applied: bool = False
    applied_at: Optional[datetime] = None
    duration_seconds: float = 0.0

class MigrationManager:
    def __init__(self, migrations_dir: str = MIGRATIONS_DIR):
        self.migrations_dir = migrations_dir
        self.applied_migrations = set()
        self.migrations_history: List[Migration] = []
    
    def get_migrations(self) -> List[str]:
        versions_dir = os.path.join(self.migrations_dir, "versions")
        if not os.path.exists(versions_dir):
            os.makedirs(versions_dir, exist_ok=True)
            return []
        
        migrations = []
        for filename in os.listdir(versions_dir):
            if filename.endswith('.py'):
                migrations.append(filename[:-3])
        
        return sorted(migrations)
    
    def parse_migration_file(self, filename: str) -> Dict[str, Any]:
        filepath = os.path.join(self.migrations_dir, "versions", f"{filename}.py")
        if not os.path.exists(filepath):
            return {}
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        result = {}
        for pattern in ['revision = ', 'down_revision = ']:
            match = re.search(rf"{pattern}['\"]([^'\"]*)['\"]", content)
            if match:
                key = "revision" if "revision" in pattern else "down_revision"
                result[key] = match.group(1)
        
        result['path'] = filepath
        return result
    
    def run_migration(self, migration_name: str, direction: str = "upgrade") -> bool:
        migration_info = self.parse_migration_file(migration_name)
        if not migration_info:
            logger.error(f"Migration not found: {migration_name}")
            return False
        
        filepath = migration_info['path']
        
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            
            try:
                import psycopg2
                conn = psycopg2.connect(DATABASE_URL)
                cur = conn.cursor()
                
                if direction == "upgrade":
                    if 'def upgrade():' in content:
                        exec_globals = {'op': _AlembicOps(conn), 'sa': __import__('sqlalchemy'), 'postgresql': __import__('sqlalchemy.dialects.postgresql')}
                        code = content.split('def downgrade():')[0]
                        exec(code, exec_globals)
                        if 'upgrade' in exec_globals:
                            exec_globals['upgrade']()
                elif direction == "downgrade":
                    if 'def downgrade():' in content:
                        exec_globals = {'op': _AlembicOps(conn), 'sa': __import__('sqlalchemy')}
                        code = content.split('def downgrade():')[1].strip()
                        exec(code, exec_globals)
                
                conn.commit()
                cur.close()
                conn.close()
                return True
            except ImportError:
                sql_file = f"/tmp/{migration_name}.sql"
                sql_content = []
                in_upgrade = False
                for line in content.split('\n'):
                    if 'def upgrade():' in line:
                        in_upgrade = True
                        continue
                    if 'def downgrade():' in line:
                        break
                    if in_upgrade and not line.strip().startswith('#') and not line.strip().startswith('def ') and not 'import ' in line:
                        sql_content.append(line)
                
                with open(sql_file, 'w') as f:
                    f.write('\n'.join(sql_content))
                return run_sql_migration(sql_file)
            
        except Exception as e:
            logger.error(f"Migration failed: {e}")
            import traceback
            traceback.print_exc()
            return False

class _AlembicOps:
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()
    
    def create_table(self, name, *args, **kwargs):
        cols = []
        for col in args[0]:
            if hasattr(col, 'name'):
                col_def = f"{col.name} {self._type_sql(col.type)}"
                if col.nullable == False:
                    col_def += " NOT NULL"
                if hasattr(col, 'default') and col.default is not None:
                    if hasattr(col.default, 'arg'):
                        col_def += f" DEFAULT {col.default.arg}"
                cols.append(col_def)
        
        pk = "PRIMARY KEY"
        pkey_idx = ""
        pkey_idx = f", PRIMARY KEY ({kwargs.get('pkey', 'id')})"
        
        sql = f"CREATE TABLE {name} ({', '.join(cols)}{pkey_idx if pkey_idx else ''})"
        self.cur.execute(sql)
    
    def add_column(self, table, column, *args, **kwargs):
        col_sql = f"ALTER TABLE {table} ADD COLUMN {column.name}"
        if hasattr(column, 'type'):
            col_sql += f" {self._type_sql(column.type)}"
        if hasattr(column, 'nullable') and not column.nullable:
            col_sql += " NOT NULL"
        if hasattr(column, 'server_default') and column.server_default:
            col_sql += f" DEFAULT {column.server_default}"
        self.cur.execute(col_sql)
    
    def drop_column(self, table, column):
        self.cur.execute(f"ALTER TABLE {table} DROP COLUMN {column}")
    
    def create_index(self, name, table, *args):
        cols = args[0] if args else []
        if isinstance(cols, str):
            cols = [cols]
        cols_str = ', '.join(cols)
        self.cur.execute(f"CREATE INDEX {name} ON {table} ({cols_str})")
    
    def drop_index(self, name, table=None):
        if table:
            self.cur.execute(f"DROP INDEX {name}")
    
    def _type_sql(self, type_obj):
        type_str = str(type_obj)
        type_map = {
            'String': 'TEXT',
            'Integer': 'INTEGER',
            'Float': 'DOUBLE PRECISION',
            'Boolean': 'BOOLEAN',
            'DateTime': 'TIMESTAMP WITH TIME ZONE',
            'Text': 'TEXT',
            'UUID': 'UUID',
            'JSONB': 'JSONB',
        }
        for py_type, sql_type in type_map.items():
            if py_type in type_str:
                return sql_type
        return 'TEXT'
    
    def create_migration(self, name: str) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        revision = f"{name}_{timestamp}"
        versions_dir = os.path.join(self.migrations_dir, "versions")
        os.makedirs(versions_dir, exist_ok=True)
        
        template = f'''"""{name}"""

revision = '{revision}'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    pass

def downgrade():
    pass
'''
        
        filepath = os.path.join(versions_dir, f"{revision}.py")
        with open(filepath, 'w') as f:
            f.write(template)
        
        logger.info(f"Created migration: {revision}")
        return revision

def run_sql_migration(sql_file: str) -> bool:
    try:
        with open(sql_file, 'r') as f:
            sql = f.read()
        
        cmd = f"psql {DATABASE_URL} -f {sql_file}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            logger.info(f"SQL migration ran successfully")
            return True
        else:
            logger.error(f"SQL migration failed: {result.stderr}")
            return False
    except Exception as e:
        logger.error(f"SQL migration error: {e}")
        return False

def status():
    manager = MigrationManager()
    migrations = manager.get_migrations()
    
    print("=" * 60)
    print("SalesGenie Database Migration Status")
    print("=" * 60)
    print(f"Migrations Directory: {manager.migrations_dir}")
    print(f"Database URL: {DATABASE_URL}")
    print("-" * 60)
    
    for name in migrations:
        info = manager.parse_migration_file(name)
        print(f"  {name}")
        print(f"    Revision: {info.get('revision', 'N/A')}")
        print(f"    Down Revision: {info.get('down_revision', 'None')}")
        print()
    
    print(f"Total migrations: {len(migrations)}")

def upgrade(target: str = "head"):
    manager = MigrationManager()
    migrations = manager.get_migrations()
    
    print("=" * 60)
    print("Running Database Migrations")
    print("=" * 60)
    
    for name in migrations:
        print(f"Migrating: {name}")
        success = manager.run_migration(name, "upgrade")
        status = "✓ OK" if success else "✗ FAILED"
        print(f"  {status}")
        print()
    
    print("=" * 60)
    print("Migrations Complete")
    print("=" * 60)

def downgrade(target: str = "-1"):
    manager = MigrationManager()
    migrations = manager.get_migrations()
    
    if target == "-1":
        target = migrations[-1] if migrations else ""
    
    print(f"Rolling back to: {target}")
    
    for name in reversed(migrations):
        if name == target:
            break
        print(f"Rolling back: {name}")
        manager.run_migration(name, "downgrade")

def create_migration(name: str):
    manager = MigrationManager()
    revision = manager.create_migration(name)
    print(f"Created migration: {revision}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 migrate.py status")
        print("  python3 migrate.py upgrade [target]")
        print("  python3 migrate.py downgrade [target]")
        print("  python3 migrate.py create <migration_name>")
        print("  python3 migrate.py run <sql_file>")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "status":
        status()
    elif command == "upgrade":
        target = sys.argv[2] if len(sys.argv) > 2 else "head"
        upgrade(target)
    elif command == "downgrade":
        target = sys.argv[2] if len(sys.argv) > 2 else "-1"
        downgrade(target)
    elif command == "create":
        if len(sys.argv) < 3:
            print("Usage: python3 migrate.py create <migration_name>")
            sys.exit(1)
        create_migration(sys.argv[2])
    elif command == "run":
        if len(sys.argv) < 3:
            print("Usage: python3 migrate.py run <sql_file>")
            sys.exit(1)
        run_sql_migration(sys.argv[2])
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)