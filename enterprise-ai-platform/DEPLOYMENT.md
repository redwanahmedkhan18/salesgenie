# SalesGenie Customer Deployment Configuration

## Super Admin Setup

Each customer deployment requires creating a super admin user. This is done through the setup script:

```bash
# Set environment variables for your customer
export SALESGENIE_SUPER_ADMIN_EMAIL="admin@acme.com"
export SALESGENIE_SUPER_ADMIN_NAME="Acme Super Admin"
export SALESGENIE_SUPER_ADMIN_PASSWORD="secure-password-here"

# Run the setup script
python -m enterprise_ai_platform.scripts.setup_super_admin
```

## Frontend Configuration

For the frontend to display the correct super admin email, ensure:

1. The super admin user created in Keycloak must have the `super_admin` role
2. The user's email must match what you set in Keycloak
3. After login, the JWT token will contain the user's email and roles

## Changing the Super Admin Email

To change the super admin email for a customer:

### Option 1: Via Keycloak Admin Console
1. Login to Keycloak Admin Console at `http://localhost:8080`
2. Navigate to `SalesGenie Realm` → `Users`
3. Find the super admin user → Edit → Change email
4. Save changes

### Option 2: Via Setup Script
1. Delete the existing super admin in Keycloak
2. Re-run the setup script with the new email:
```bash
export SALESGENIE_SUPER_ADMIN_EMAIL="new-admin@acme.com"
python -m enterprise_ai_platform.scripts.setup_super_admin
```

## Production Deployment Steps

1. **Set Customer-Specific Environment Variables:**
   - `SALESGENIE_SUPER_ADMIN_EMAIL`
   - `SALESGENIE_SUPER_ADMIN_NAME`
   - `SALESGENIE_SUPER_ADMIN_PASSWORD`
   - `KEYCLOAK_ADMIN_PASSWORD` (for Keycloak admin)
   - `JWT_SECRET_KEY` (unique per customer)

2. **Deploy Keycloak with Customer Realm**

3. **Run Super Admin Setup Script**

4. **Verify Login Works at `http://[customer-domain]:4321`**

## No Hardcoded Values

The application has no hardcoded super admin emails. All user information comes from:
- Keycloak user store (email, name)
- JWT token payload
- Auth context via `useAuth()` hook

The `admin@salesgenie.ai` string only appears as a **fallback UI text** when user data is not yet loaded.

## Testing the Setup

After running the setup script, login with:
- Email: `$SALESGENIE_SUPER_ADMIN_EMAIL`
- Password: `$SALESGENIE_SUPER_ADMIN_PASSWORD`

The dashboard should now show:
- User's actual name in the sidebar
- User's actual email in the sidebar
- Full super admin privileges (access to all sections)