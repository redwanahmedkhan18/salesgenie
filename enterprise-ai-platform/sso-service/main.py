"""SalesGenie SSO Integration Service - Azure AD, Okta, Google Workspace"""

import hashlib
import json
import logging
import os
import time
from typing import Dict, Optional, Any
from datetime import datetime, timedelta
import base64
import hmac

logger = logging.getLogger("sso_service")

class AzureADClient:
    """Microsoft Azure Active Directory Integration"""
    
    def __init__(self, tenant_id: str, client_id: str, client_secret: str, redirect_uri: str):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.base_url = f"https://login.microsoftonline.com/{tenant_id}"
    
    def get_authorization_url(self, state: str) -> str:
        """Generate Azure AD authorization URL"""
        params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_uri,
            'scope': 'openid email profile offline_access',
            'response_mode': 'query',
            'state': state,
            'prompt': 'select_account'
        }
        
        query = '&'.join([f"{k}={v}" for k, v in params.items()])
        return f"{self.base_url}/oauth2/v2.0/authorize?{query}"
    
    async def exchange_code(self, code: str) -> Dict:
        """Exchange authorization code for tokens"""
        import aiohttp
        token_url = f"{self.base_url}/oauth2/v2.0/token"
        data = {
            'client_id': self.client_id,
            'scope': 'openid email profile offline_access',
            'code': code,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code',
            'client_secret': self.client_secret
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(token_url, data=data) as response:
                return await response.json()

class OktaClient:
    """Okta SSO Integration"""
    
    def __init__(self, org_url: str, client_id: str, client_secret: str, redirect_uri: str):
        self.org_url = org_url.rstrip('/')
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.base_url = f"{self.org_url}/oauth2/default"
    
    def get_authorization_url(self, state: str) -> str:
        """Generate Okta authorization URL"""
        params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_uri,
            'scope': 'openid email profile groups',
            'response_mode': 'query',
            'state': state
        }
        
        query = '&'.join([f"{k}={v}" for k, v in params.items()])
        return f"{self.base_url}/v1/authorize?{query}"
    
    async def exchange_code(self, code: str) -> Dict:
        """Exchange authorization code for tokens"""
        import aiohttp
        token_url = f"{self.base_url}/v1/token"
        
        credentials = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
        
        async with aiohttp.ClientSession() as session:
            async with session.post(token_url, 
                headers={'Authorization': f'Basic {credentials}'},
                data={
                    'grant_type': 'authorization_code',
                    'code': code,
                    'redirect_uri': self.redirect_uri
                }) as response:
                return await response.json()

class GoogleWorkspaceClient:
    """Google Workspace (G-Suite) Integration"""
    
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, domain: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.domain = domain
        self.base_url = "https://accounts.google.com"
    
    def get_authorization_url(self, state: str) -> str:
        """Generate Google authorization URL"""
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'response_type': 'code',
            'scope': 'openid email profile https://www.googleapis.com/auth/admin.directory.user.readonly',
            'access_type': 'offline',
            'prompt': 'consent',
            'state': state,
            'hd': self.domain
        }
        
        query = '&'.join([f"{k}={v}" for k, v in params.items()])
        return f"{self.base_url}/o/oauth2/v2/auth?{query}"
    
    async def exchange_code(self, code: str) -> Dict:
        """Exchange authorization code for tokens"""
        import aiohttp
        token_url = f"{self.base_url}/o/oauth2/v4/token"
        
        async with aiohttp.ClientSession() as session:
            async with session.post(token_url, data={
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'redirect_uri': self.redirect_uri,
                'grant_type': 'authorization_code',
                'code': code
            }) as response:
                return await response.json()

class SSOService:
    """Master SSO Service orchestrating all providers"""
    
    def __init__(self):
        self.azure_ad: Optional[AzureADClient] = None
        self.okta: Optional[OktaClient] = None
        self.google: Optional[GoogleWorkspaceClient] = None
        self.active_provider: str = ""
    
    def configure(self, provider: str, **kwargs):
        """Configure SSO provider"""
        if provider == "azure_ad":
            self.azure_ad = AzureADClient(
                tenant_id=kwargs.get('tenant_id'),
                client_id=kwargs.get('client_id'),
                client_secret=kwargs.get('client_secret'),
                redirect_uri=kwargs.get('redirect_uri')
            )
            self.active_provider = "azure_ad"
        elif provider == "okta":
            self.okta = OktaClient(
                org_url=kwargs.get('org_url'),
                client_id=kwargs.get('client_id'),
                client_secret=kwargs.get('client_secret'),
                redirect_uri=kwargs.get('redirect_uri')
            )
            self.active_provider = "okta"
        elif provider == "google":
            self.google = GoogleWorkspaceClient(
                client_id=kwargs.get('client_id'),
                client_secret=kwargs.get('client_secret'),
                redirect_uri=kwargs.get('redirect_uri'),
                domain=kwargs.get('domain')
            )
            self.active_provider = "google"
    
    def get_auth_url(self, state: str) -> str:
        """Get authorization URL for active provider"""
        if self.azure_ad and self.active_provider == "azure_ad":
            return self.azure_ad.get_authorization_url(state)
        elif self.okta and self.active_provider == "okta":
            return self.okta.get_authorization_url(state)
        elif self.google and self.active_provider == "google":
            return self.google.get_authorization_url(state)
        raise ValueError("No SSO provider configured")
    
    async def handle_callback(self, code: str) -> Dict:
        """Handle OAuth callback and return user info"""
        if self.azure_ad and self.active_provider == "azure_ad":
            tokens = await self.azure_ad.exchange_code(code)
            return await self._get_user_info_azure(tokens.get('access_token'))
        elif self.okta and self.active_provider == "okta":
            tokens = await self.okta.exchange_code(code)
            return await self._get_user_info_okta(tokens.get('access_token'))
        elif self.google and self.active_provider == "google":
            tokens = await self.google.exchange_code(code)
            return await self._get_user_info_google(tokens.get('access_token'))
        raise ValueError("No SSO provider configured")
    
    async def _get_user_info_azure(self, access_token: str) -> Dict:
        """Get user info from Microsoft Graph"""
        import aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://graph.microsoft.com/v1.0/me",
                headers={'Authorization': f'Bearer {access_token}'}
            ) as response:
                user = await response.json()
                return {
                    'email': user.get('mail', user.get('userPrincipalName')),
                    'name': user.get('displayName'),
                    'provider': 'azure_ad',
                    'id': user.get('id')
                }

def create_app():
    """Create FastAPI app for SSO Service"""
    from fastapi import FastAPI, Request, HTTPException
    from fastapi.responses import RedirectResponse, JSONResponse
    
    app = FastAPI(title="SSO Service", version="1.0.0")
    sso = SSOService()
    sessions = {}
    
    @app.get("/health")
    async def health_check():
        return {"status": "healthy", "service": "sso", "providers": ["azure_ad", "okta", "google"]}
    
    @app.get("/auth/{provider}/login")
    async def login(provider: str, request: Request):
        state = hashlib.sha256(f"{time.time()}{os.urandom(16)}".encode()).hexdigest()[:16]
        sessions[state] = {'provider': provider, 'created': time.time()}
        
        sso.configure(provider,
            tenant_id=os.environ.get('AZURE_TENANT_ID', ''),
            client_id=os.environ.get('AZURE_CLIENT_ID', ''),
            client_secret=os.environ.get('AZURE_CLIENT_SECRET', ''),
            redirect_uri=str(request.url).replace('/login', '/callback')
        )
        
        auth_url = sso.get_auth_url(state)
        return RedirectResponse(auth_url)
    
    @app.get("/auth/{provider}/callback")
    async def callback(provider: str, code: str, state: str):
        if state not in sessions:
            raise HTTPException(status_code=400, detail="Invalid state")
        
        try:
            user_info = await sso.handle_callback(code)
            token = hashlib.sha256(f"{user_info['id']}{time.time()}".encode()).hexdigest()[:32]
            return JSONResponse({'token': token, 'user': user_info})
        except Exception as e:
            raise HTTPException(status_code=401, detail=str(e))
    
    return app

if __name__ == "__main__":
    app = create_app()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8028)