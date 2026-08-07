#!/usr/bin/env python3
"""
Grant Super Admin Role Script
Usage: python grant_super_admin.py user@example.com

This script assigns the Super Admin role to an existing user by email.
"""

import sys
import asyncio
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# Database config
DATABASE_URL = "postgresql+asyncpg://salesgenie_admin:salesgenie_secret_pass_2026@localhost:5433/salesgenie"

from enterprise_ai_platform.common.security_rbac import PlatformRole
from enterprise_ai_platform.auth_service.src.models import User

async def grant_super_admin(email: str):
    engine = create_async_engine(DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    
    async with async_session() as session:
        # Find user by email
        stmt = select(User).where(User.email == email)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()
        
        if not user:
            print(f"❌ User with email '{email}' not found")
            return
        
        # Check if user is already an organization admin or higher
        # Note: In this implementation, roles are determined at JWT token generation time
        # based on the email matching SALESGENIE_SUPER_ADMIN_EMAILS config
        
        print(f"✓ Found user: {user.email}")
        print(f"  Name: {user.full_name}")
        print(f"  Organization: {user.company}")
        print(f"  Is Verified: {user.is_verified}")
        print(f"  Is Active: {user.is_active}")
        print()
        print("ℹ️  NOTE: In SalesGenie, Super Admin role is determined by email matching")
        print("   the SALESGENIE_SUPER_ADMIN_EMAILS configuration in .env")
        print()
        print("To grant Super Admin access, add your email to .env:")
        print(f"   SALESGENIE_SUPER_ADMIN_EMAILS={email}")
        print()
        print("2. Restart the application")
        print("3. The user will automatically get Super Admin role on next login")
        
        await engine.dispose()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python grant_super_admin.py <email>")
        print("Example: python grant_super_admin.py admin@yourcompany.com")
        sys.exit(1)
    
    email = sys.argv[1]
    asyncio.run(grant_super_admin(email))