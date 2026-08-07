#!/bin/bash
# Super Admin Setup Script
# Run this script to set your email as a Super Admin for the SalesGenie platform

echo "=========================================="
echo "  SalesGenie Super Admin Setup"
echo "=========================================="
echo ""
echo "This will configure YOUR email to have Super Admin privileges."
echo ""

read -p "Enter your email address (this will be a Super Admin): " ADMIN_EMAIL

if [ -z "$ADMIN_EMAIL" ]; then
    echo "Error: Email is required"
    exit 1
fi

# Update .env file
if grep -q "SALESGENIE_SUPER_ADMIN_EMAIL=" /home/user/salesgenie/.env; then
    # Uncomment and update existing line
    sed -i "s/# SALESGENIE_SUPER_ADMIN_EMAIL=.*/SALESGENIE_SUPER_ADMIN_EMAIL=$ADMIN_EMAIL/" /home/user/salesgenie/.env
else
    # Add new line after SAMLESGENIE_SUPER_ADMIN_EMAILS line
    sed -i "/SALESGENIE_SUPER_ADMIN_EMAILS/a # SALESGENIE_SUPER_ADMIN_EMAIL=$ADMIN_EMAIL" /home/user/salesgenie/.env
fi

echo ""
echo "✓ Updated .env file"
echo ""
echo "Next steps:"
echo "1. Restart the application (run dev server again)"
echo "2. Sign up with $ADMIN_EMAIL will automatically get Super Admin role"
echo ""
echo "Or to manually upgrade an existing user:"
echo "  Run: python /home/user/salesgenie/enterprise-ai-platform/scripts/grant_super_admin.py $ADMIN_EMAIL"
echo ""