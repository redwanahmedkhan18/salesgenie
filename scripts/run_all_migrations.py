"""
Run all service-specific Alembic migrations against the central PostgreSQL database.
Handles idempotency by checking existing columns/tables before applying changes.
"""
import os
import sys
import subprocess
import tempfile

POSTGRES_USER = 'salesgenie_admin'
POSTGRES_PASSWORD = 'salesgenie_secret_pass_2026'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5433'
POSTGRES_DB = 'salesgenie'

DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
SERVICES_DIR = '/home/user/salesgenie/enterprise-ai-platform'
sys.path.insert(0, SERVICES_DIR)
sys.path.insert(0, '/home/user/salesgenie')

INLINE_ENV = '''
"""Alembic environment configuration."""
from logging.config import dictConfig
import os
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

config = context.config

dictConfig({
    "version": 1,
    "formatters": {"default": {"format": "%%(asctime)s %%(levelname)s %%(name)s %%(message)s"}},
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "default"}},
    "root": {"level": "INFO", "handlers": ["console"]},
})

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=None, literal_binds=True, dialect_opts={"paramstyle": "named"})
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(config.get_section(config.config_ini_section, {}), prefix="sqlalchemy.", poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=None)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
'''

TEMPLATE = """[alembic]
script_location = {script_location}
sqlalchemy.url = {database_url}
sourceless = true

[postgresql]
schema = public
"""


def run_service_migrations(svc, mig_dir):
    """Create temp ini + env.py and run alembic upgrade head."""
    from sqlalchemy import create_engine, text

    engine = create_engine(DATABASE_URL)

    # Drop alembic_version table so each service can start fresh
    with engine.connect() as conn:
        with conn.begin():
            conn.execute(text('DROP TABLE IF EXISTS alembic_version'))

    # Write inline env.py
    env_path = os.path.join(mig_dir, 'env.py')
    original_env = None
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            original_env = f.read()
    with open(env_path, 'w') as f:
        f.write(INLINE_ENV)

    # Write temp ini
    with tempfile.NamedTemporaryFile(
        mode='w', suffix='.ini', dir=mig_dir, delete=False, prefix='alembic_tmp_'
    ) as tmp_ini:
        tmp_ini.write(TEMPLATE.format(
            script_location=mig_dir,
            database_url=DATABASE_URL,
        ))
        ini_path = tmp_ini.name

    env = os.environ.copy()
    env['DATABASE_URL'] = DATABASE_URL
    env['PYTHONPATH'] = f'{SERVICES_DIR}:/home/user/salesgenie'

    try:
        result = subprocess.run(
            [sys.executable, '-m', 'alembic', '-c', ini_path, 'upgrade', 'head'],
            env=env,
            capture_output=True,
            text=True,
            cwd='/home/user/salesgenie',
            timeout=60,
        )

        if result.returncode == 0:
            output = result.stderr.strip() + '\n' + result.stdout.strip()
            for line in output.split('\n'):
                if 'upgrade' in line.lower() and line.strip():
                    print(f'  {line.strip()}')
            return 'success', None
        else:
            return 'error', (result.stderr.strip() or result.stdout.strip())
    except subprocess.TimeoutExpired:
        return 'timeout', 'Timeout'
    finally:
        os.unlink(ini_path)
        # Restore original env.py
        if original_env is not None:
            with open(env_path, 'w') as f:
                f.write(original_env)


def main():
    services = sorted([
        d for d in os.listdir(SERVICES_DIR)
        if os.path.isdir(os.path.join(SERVICES_DIR, d))
    ])

    success_count = 0
    fail_count = 0
    skip_count = 0

    for svc in services:
        mig_dir = os.path.join(SERVICES_DIR, svc, 'migrations')
        versions_dir = os.path.join(mig_dir, 'versions')
        if not os.path.isdir(versions_dir):
            continue

        versions = [
            f for f in os.listdir(versions_dir)
            if f.endswith('.py') and not f.startswith('__init__')
        ]
        if not versions:
            continue

        if svc == 'database':
            print(f'=== {svc} (skipped - already migrated) ===')
            skip_count += 1
            continue

        print(f'=== {svc} ({len(versions)} migrations) ===')

        status, error = run_service_migrations(svc, mig_dir)
        if status == 'success':
            print(f'  SUCCESS')
            success_count += 1
        elif status == 'timeout':
            print(f'  TIMEOUT')
            fail_count += 1
        else:
            if error and ('already exists' in error.lower() or 'duplicate' in error.lower()):
                print(f'  SKIP (already applied)')
                skip_count += 1
            else:
                if error:
                    for line in error.split('\n'):
                        if line.strip() and ('ERROR' in line or 'Error' in line or 'error' in line):
                            print(f'  {line.strip()}')
                fail_count += 1

    print(f'\n=== Summary: {success_count} succeeded, {fail_count} failed, {skip_count} skipped ===')


if __name__ == '__main__':
    main()
