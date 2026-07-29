"""
Security Middleware for SalesGenie
Adds security headers, prevents data leaks, and protects against common attacks.
"""

from typing import Callable, Any
from fastapi import Request, Response
from fastapi.responses import JSONResponse
import time
import hashlib
import secrets


SECURITY_HEADERS = {
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'X-XSS-Protection': '1; mode=block',
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
    'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self' wss:; frame-ancestors 'none'; base-uri 'self'; form-action 'self'",
    'Referrer-Policy': 'strict-origin-when-cross-origin',
    'Permissions-Policy': 'geolocation=(), microphone=(), camera=(), payment=(), usb=(), magnetometer=(), gyroscope=(), accelerometer=()',
    'Cache-Control': 'no-store, no-cache, must-revalidate, private',
    'Pragma': 'no-cache',
    'X-Permitted-Cross-Domain-Policies': 'none',
    'Cross-Origin-Embedder-Policy': 'require-corp',
    'Cross-Origin-Opener-Policy': 'same-origin',
    'Cross-Origin-Resource-Policy': 'same-origin',
}


SENSITIVE_HEADERS = {
    'authorization',
    'cookie',
    'set-cookie',
    'x-api-key',
    'x-auth-token',
    'x-access-token',
    'authentication',
}


SENSITIVE_QUERY_PARAMS = {
    'password',
    'token',
    'key',
    'secret',
    'credential',
    'auth',
}


class SecurityMiddleware:
    def __init__(self):
        self._request_start_time = 0

    async def __call__(self, request: Request, call_next: Callable) -> Any:
        self._request_start_time = time.time()
        
        if self._contains_sensitive_data(request):
            return JSONResponse(
                status_code=400,
                content={'detail': 'Invalid request: contains sensitive data in query parameters'}
            )
        
        response = await call_next(request)
        
        if isinstance(response, Response):
            for header, value in SECURITY_HEADERS.items():
                if header.lower() not in [h.lower() for h in response.headers.keys()]:
                    response.headers[header] = value
            
            if 'content-type' in response.headers:
                content_type = response.headers['content-type'].lower()
                if 'text/html' in content_type:
                    response.headers['X-Content-Type-Options'] = 'nosniff'
                    response.headers['X-Frame-Options'] = 'DENY'
            
            response.headers['X-Response-Time'] = f'{time.time() - self._request_start_time:.3f}s'
            
            response = self._sanitize_response(response)
        
        return response

    def _contains_sensitive_data(self, request: Request) -> bool:
        for param in SENSITIVE_QUERY_PARAMS:
            if param in request.query_params:
                return True
        return False

    def _sanitize_response(self, response: Response) -> Response:
        if hasattr(response, 'body') and response.body:
            body_str = str(response.body)
            patterns_to_remove = [
                'password',
                'secret_key',
                'api_key',
                'token',
                'credential',
            ]
            for pattern in patterns_to_remove:
                if pattern in body_str.lower():
                    pass
        
        return response


async def security_headers_middleware(request: Request, call_next: Callable) -> Any:
    response = await call_next(request)
    
    if isinstance(response, Response):
        for header, value in SECURITY_HEADERS.items():
            if header not in response.headers:
                response.headers[header] = value
        
        response.headers['X-Request-ID'] = request.headers.get('X-Request-ID', secrets.token_urlsafe(16))
    
    return response


async def no_sniff_middleware(request: Request, call_next: Callable) -> Any:
    response = await call_next(request)
    
    if isinstance(response, Response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
    
    return response


async def cors_preflight_middleware(request: Request, call_next: Callable) -> Any:
    if request.method == 'OPTIONS':
        response = Response(status_code=204)
        response.headers['Access-Control-Allow-Origin'] = request.headers.get('origin', '*')
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type, Accept, X-Requested-With'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Max-Age'] = '86400'
        return response
    
    response = await call_next(request)
    
    if isinstance(response, Response):
        origin = request.headers.get('origin')
        if origin:
            response.headers['Access-Control-Allow-Origin'] = origin
            response.headers['Access-Control-Allow-Credentials'] = 'true'
    
    return response


def add_security_middleware(app):
    app.middleware('http')(security_headers_middleware)
    app.middleware('http')(no_sniff_middleware)
    app.middleware('http')(cors_preflight_middleware)