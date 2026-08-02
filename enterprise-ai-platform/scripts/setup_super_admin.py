#!/usr/bin/env python3
"""
SalesGenie Super Admin Setup Script
Run this script after deployment to create your first super admin user.

Usage:
    python -m scripts.setup_super_admin

Environment variables can be set to customize the super admin:
    SALESGENIE_SUPER_ADMIN_EMAIL - Email for the super admin (default: admin@yourcompany.com)
    SALESGENIE_SUPER_ADMIN_NAME - Full name for the super admin (default: Super Admin)
    SALESGENIE_SUPER_ADMIN_PASSWORD - Password for the super admin (required)
"""

import os
import asyncio
import uuid
from datetime import datetime, timezone

# These will be replaced by actual imports from the platform
try:
    from enterprise_ai_platform.common.config import settings
    from enterprise_ai_platform.common.security_rbac import PlatformRole
    from enterprise_ai_platform.auth_service.src.keycloak_client import keycloak_client
except ImportError:
    print("Please run this script from the project root directory")
    exit(1)

SUPER_ADMIN_EMAIL = os.environ.get('SALESGENIE_SUPER_ADMIN_EMAIL', 'admin@yourcompany.com')
SUPER_ADMIN_NAME = os.environ.get('SALESGENIE_SUPER_ADMIN_NAME', 'Super Admin')
SUPER_ADMIN_PASSWORD = os.environ.get('SALESGENIE_SUPER_ADMIN_PASSWORD')

if not SUPER_ADMIN_PASSWORD:
    print("ERROR: SALESGENIE_SUPER_ADMIN_PASSWORD environment variable is required")
    print("Example: export SALESGENIE_SUPER_ADMIN_PASSWORD='secure-password-here'")
    exit(1)


async def create_super_admin():
    """Create a super admin user in Keycloak and return credentials."""
    
    user_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, SUPER_ADMIN_EMAIL))
    
    # Check if user already exists
    try:
        existing_user = await keycloak_client.get_user_by_email(SUPER_ADMIN_EMAIL)
        if existing_user:
            print(f"Super admin user already exists: {SUPER_ADMIN_EMAIL}")
            return {
                'email': SUPER_ADMIN_EMAIL,
                'user_id': user_id,
                'status': 'exists'
            }
    except Exception as e:
        print(f"Warning: Could not check existing users: {e}")
    
    # Create user in Keycloak
    try:
        user = await keycloak_client.create_user({
            'email': SUPER_ADMIN_EMAIL,
            'username': SUPER_ADMIN_EMAIL,
            'enabled': True,
            'fullName': SUPER_ADMIN_NAME,
            'firstName': SUPER_ADMIN_NAME.split()[0] if SUPER_ADMIN_NAME else 'Admin',
            'lastName': ' '.join(SUPER_ADMIN_NAME.split()[1:]) if len(SUPER_ADMIN_NAME.split()) > 1 else 'Admin',
        })
        
        # Set password
        await keycloak_client.set_password(user['id'], SUPER_ADMIN_PASSWORD)
        
        # Assign super_admin role
        await keycloak_client.assign_realm_role(user['id'], 'super_admin')
        
        print(f"✓ Created super admin user: {SUPER_ADMIN_EMAIL}")
        print(f"  User ID: {user_id}")
        print(f"  Name: {SUPER_ADMIN_NAME}")
        
        return {
            'email': SUPER_ADMIN_EMAIL,
            'user_id': user_id,
            'name': SUPER_ADMIN_NAME,
            'status': 'created'
        }
        
    except Exception as e:
        print(f"ERROR: Failed to create super admin: {e}")
        return {'error': str(e), 'status': 'failed'}


async def test_login(email: str, password: str):
    """Test that the super admin can login."""
    try:
        from enterprise_ai_platform.auth_service.src.keycloak_client import keycloak_client
        token = await keycloak_client.authenticate_user_credentials(email, password)
        if token:
            print(f"✓ Successfully tested login for {email}")
            return True
    except Exception as e:
        print(f"ERROR: Login test failed: {e}")
        return False
    return False


async def main():
    print("=" * 60)
    print("SalesGenie Super Admin Setup")
    print("=" * 60)
    print(f"\nTarget Email: {SUPER_ADMIN_EMAIL}")
    print(f"Target Name: {SUPER_ADMIN_NAME}")
    print(f"Keycloak URL: {settings.KEYCLOAK_SERVER_URL}")
    print(f"Keycloak Realm: {settings.KEYCLOAK_REALM}")
    print()
    
    # Create super admin
    result = await create_super_admin()
    
    if result.get('status') in ['created', 'exists']:
        print("\n" + "=" * 60)
        print("SUPER ADMIN READY")
        print("=" * 60)
        print(f"\nLogin with:")
        print(f"  Email: {SUPER_ADMIN_EMAIL}")
        print(f"  Password: {SUPER_ADMIN_PASSWORD}")
        print(f"\nNote: Keep your password secure and store it securely!")
        
        # Test login
        await test_login(SUPER_ADMIN_EMAIL, SUPER_ADMIN_PASSWORD)
    else:
        print(f"\nFailed to create super admin: {result}")
        exit(1)


if __name__ == '__main__':
    asyncio.run(main())