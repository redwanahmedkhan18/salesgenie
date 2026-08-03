"""Instagram Integration Service for SalesGenie Platform"""

import hashlib
import hmac
import json
import logging
import os
import time
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import asyncio

logger = logging.getLogger("instagram_service")

class InstagramClient:
    """Instagram Graph API Client"""
    
    def __init__(self, access_token: str, app_secret: str, business_account_id: str):
        self.access_token = access_token
        self.app_secret = app_secret
        self.business_account_id = business_account_id
        self.base_url = "https://graph.instagram.com/v18.0"
        self.rate_limit_remaining = 100
        self.rate_limit_reset = 0
    
    async def _make_request(self, endpoint: str, params: Dict = None) -> Dict:
        """Make API request with rate limiting and retry logic"""
        if time.time() < self.rate_limit_reset:
            await asyncio.sleep(self.rate_limit_reset - time.time())
        
        url = f"{self.base_url}/{self.business_account_id}/{endpoint}"
        params = params or {}
        params['access_token'] = self.access_token
        
        import aiohttp
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    data = await response.json()
                    self.rate_limit_remaining = int(response.headers.get('X-Instagram-Rate-Limit-Remaining', 100))
                    self.rate_limit_reset = time.time() + int(response.headers.get('X-Instagram-Rate-Limit-Reset', 60))
                    return data
        except Exception as e:
            logger.error(f"Instagram API request failed: {e}")
            raise
    
    async def get_media(self, limit: int = 25, after: str = None) -> Dict:
        """Fetch recent media from Instagram Business Account"""
        params = {'fields': 'id,caption,media_type,media_url,permalink,timestamp,like_count,comment_count', 'limit': limit}
        if after:
            params['after'] = after
        return await self._make_request('media', params)
    
    async def get_comments(self, media_id: str) -> Dict:
        """Fetch comments for a specific media"""
        return await self._make_request(f'{media_id}/comments', {'fields': 'id,text,username,timestamp'})
    
    async def post_comment(self, media_id: str, message: str) -> Dict:
        """Post a comment on media"""
        params = {'message': message, 'access_token': self.access_token}
        import aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/{media_id}/comments", params=params) as response:
                return await response.json()
    
    async def get_tags(self) -> Dict:
        """Get tagged media"""
        return await self._make_request('tags', {'fields': 'id,caption,media_type,media_url'})
    
    async def get_insights(self) -> Dict:
        """Get business account insights"""
        return await self._make_request('insights', {
            'metric': 'impressions,reach,profile_views,website_clicks',
            'period': 'day'
        })

class InstagramService:
    """SalesGenie Instagram Integration Service"""
    
    def __init__(self):
        self.client: Optional[InstagramClient] = None
        self.webhook_secret = os.environ.get('INSTAGRAM_WEBHOOK_SECRET', '')
        self.verified_tasks = set()
        self.message_queue = []
    
    def setup(self, token: str, app_secret: str, business_account_id: str):
        """Initialize Instagram client"""
        self.client = InstagramClient(token, app_secret, business_account_id)
    
    async def fetch_posts(self, limit: int = 50) -> List[Dict]:
        """Fetch Instagram posts for integration"""
        if not self.client:
            raise ValueError("Instagram client not initialized")
        
        try:
            data = await self.client.get_media(limit=limit)
            posts = []
            for item in data.get('data', []):
                posts.append({
                    'id': item.get('id'),
                    'caption': item.get('caption', ''),
                    'media_type': item.get('media_type', 'IMAGE'),
                    'media_url': item.get('media_url'),
                    'permalink': item.get('permalink'),
                    'timestamp': item.get('timestamp'),
                    'metrics': {
                        'likes': item.get('like_count', 0),
                        'comments': item.get('comment_count', 0)
                    }
                })
            return posts
        except Exception as e:
            logger.error(f"Failed to fetch Instagram posts: {e}")
            return []
    
    async def handle_webhook(self, request_body: str, signature: str) -> Dict:
        """Verify and process Instagram webhook"""
        if not self._verify_webhook(request_body, signature):
            return {'error': 'Invalid signature'}
        
        try:
            data = json.loads(request_body)
            changes = data.get('entry', [{}])[0].get('changes', [])
            
            for change in changes:
                field = change.get('field')
                value = change.get('value')
                
                if field == 'comments':
                    await self._process_comment(value)
                elif field == 'mentions':
                    await self._process_mention(value)
            
            return {'status': 'success', 'processed': len(changes)}
        except Exception as e:
            logger.error(f"Webhhook processing error: {e}")
            return {'error': str(e)}
    
    def _verify_webhook(self, body: str, signature: str) -> bool:
        """Verify webhook signature using app secret"""
        if not self.webhook_secret or not signature:
            return False
        
        expected_signature = hmac.new(
            self.webhook_secret.encode(),
            body.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return hmac.compare_digest(signature, expected_signature)
    
    async def _process_comment(self, comment_data: Dict):
        """Process incoming comment"""
        task_id = f"comment_{comment_data.get('id')}_{int(time.time())}"
        if task_id not in self.verified_tasks:
            self.verified_tasks.add(task_id)
            self.message_queue.append({
                'type': 'instagram_comment',
                'data': comment_data,
                'timestamp': datetime.now().isoformat()
            })
    
    async def _process_mention(self, mention_data: Dict):
        """Process incoming mention"""
        self.message_queue.append({
            'type': 'instagram_mention',
            'data': mention_data,
            'timestamp': datetime.now().isoformat()
        })
    
    async def get_messages(self) -> List[Dict]:
        """Get queued messages"""
        return self.message_queue.copy()
    
    def clear_messages(self):
        """Clear processed messages"""
        self.message_queue.clear()

def create_app():
    """Create FastAPI app for Instagram Service"""
    from fastapi import FastAPI, Request, Header, HTTPException
    from fastapi.responses import JSONResponse
    import uvicorn
    
    app = FastAPI(title="Instagram Integration Service", version="1.0.0")
    instagram_service = InstagramService()
    
    @app.on_event("startup")
    async def startup_event():
        token = os.environ.get('INSTAGRAM_ACCESS_TOKEN', '')
        app_secret = os.environ.get('INSTAGRAM_APP_SECRET', '')
        business_id = os.environ.get('INSTAGRAM_BUSINESS_ACCOUNT_ID', '')
        if token and app_secret and business_id:
            instagram_service.setup(token, app_secret, business_id)
            logger.info("Instagram Service initialized")
    
    @app.get("/health")
    async def health_check():
        return {"status": "healthy", "service": "instagram", "version": "1.0.0"}
    
    @app.get("/api/v1/instagram/posts")
    async def get_posts(limit: int = 50):
        posts = await instagram_service.fetch_posts(limit=limit)
        return {"posts": posts, "count": len(posts)}
    
    @app.post("/api/v1/instagram/webhook")
    async def instagram_webhook(request: Request, x_hub_signature: str = Header(None)):
        body = await request.body()
        result = await instagram_service.handle_webhook(body.decode(), x_hub_signature)
        if 'error' in result:
            raise HTTPException(status_code=400, detail=result['error'])
        return JSONResponse(result)
    
    @app.get("/api/v1/instagram/messages")
    async def get_messages():
        messages = instagram_service.get_messages()
        instagram_service.clear_messages()
        return {"messages": messages}
    
    @app.post("/api/v1/instagram/comments/{media_id}")
    async def post_comment(media_id: str, message: str):
        if not instagram_service.client:
            raise HTTPException(status_code=503, detail="Instagram not configured")
        result = await instagram_service.client.post_comment(media_id, message)
        return result
    
    return app

if __name__ == "__main__":
    app = create_app()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8027)