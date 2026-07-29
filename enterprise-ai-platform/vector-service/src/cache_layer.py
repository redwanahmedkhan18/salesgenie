"""
Redis Cache Layer for Vector Service
Implements caching for embeddings, queries, and reranked results.
"""

import json
import hashlib
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import asyncio

try:
    import redis.asyncio as redis
    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False


@dataclass
class CacheConfig:
    """Cache configuration settings."""
    ttl_embeddings: int = 3600
    ttl_queries: int = 900
    ttl_rerank: int = 1800
    max_embedding_cache_size: int = 10000
    max_query_cache_size: int = 5000


class RedisCache:
    """
    Redis-based caching layer for vector service.
    Caches embeddings, query results, and reranked outputs.
    """

    def __init__(self, redis_url: str, config: Optional[CacheConfig] = None):
        self.config = config or CacheConfig()
        self.redis_url = redis_url
        self._client: Optional[redis.Redis] = None
        self._initialized = False

    def _get_client(self) -> redis.Redis:
        """Get or create Redis client."""
        if not REDIS_AVAILABLE:
            raise RuntimeError("Redis not available. Install redis package.")
        
        if self._client is None:
            self._client = redis.from_url(self.redis_url)
            self._initialized = True
        
        return self._client

    def _hash_key(self, key: str) -> str:
        """Generate consistent hash for cache key."""
        return hashlib.sha256(key.encode()).hexdigest()

    async def get_embedding(self, text: str) -> Optional[List[float]]:
        """Get cached embedding for text."""
        if not self._initialized:
            return None
        
        key = f"embedding:{self._hash_key(text)}"
        client = self._get_client()
        
        cached = await client.get(key)
        if cached:
            return json.loads(cached)
        return None

    async def set_embedding(self, text: str, vector: List[float]) -> None:
        """Cache an embedding."""
        if not self._initialized:
            return
        
        key = f"embedding:{self._hash_key(text)}"
        client = self._get_client()
        
        await client.setex(
            key,
            self.config.ttl_embeddings,
            json.dumps(vector)
        )

    async def get_query_result(self, query: str, top_k: int) -> Optional[List[Dict[str, Any]]]:
        """Get cached query result."""
        if not self._initialized:
            return None
        
        key = f"query:{self._hash_key(f'{query}:{top_k}')}"
        client = self._get_client()
        
        cached = await client.get(key)
        if cached:
            return json.loads(cached)
        return None

    async def set_query_result(self, query: str, top_k: int, results: List[Dict[str, Any]]) -> None:
        """Cache a query result."""
        if not self._initialized:
            return
        
        key = f"query:{self._hash_key(f'{query}:{top_k}')}"
        client = self._get_client()
        
        await client.setex(
            key,
            self.config.ttl_queries,
            json.dumps([r.model_dump() if hasattr(r, 'model_dump') else r for r in results])
        )

    async def get_rerank_result(self, query: str, chunk_ids: List[str]) -> Optional[List[Dict[str, Any]]]:
        """Get cached rerank result."""
        if not self._initialized:
            return None
        
        key = f"rerank:{self._hash_key(f'{query}:{sorted(chunk_ids)}')}"
        client = self._get_client()
        
        cached = await client.get(key)
        if cached:
            return json.loads(cached)
        return None

    async def set_rerank_result(self, query: str, chunk_ids: List[str], results: List[Dict[str, Any]]) -> None:
        """Cache a rerank result."""
        if not self._initialized:
            return
        
        key = f"rerank:{self._hash_key(f'{query}:{sorted(chunk_ids)}')}"
        client = self._get_client()
        
        await client.setex(
            key,
            self.config.ttl_rerank,
            json.dumps(results)
        )

    async def clear_cache(self, pattern: str = "*") -> None:
        """Clear cached items matching pattern."""
        if not self._initialized:
            return
        
        client = self._get_client()
        keys = await client.keys(f"*{pattern}*")
        if keys:
            await client.delete(*keys)

    async def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        if not self._initialized:
            return {"status": "not_initialized"}
        
        client = self._get_client()
        info = await client.info()
        
        return {
            "status": "connected",
            "total_commands_processed": info.get("total_commands_processed", 0),
            "used_memory_human": info.get("used_memory_human", "unknown"),
            "connected_clients": info.get("connected_clients", 0),
        }

    async def close(self) -> None:
        """Close Redis connection."""
        if self._client:
            await self._client.close()
            self._initialized = False


cache = RedisCache(redis_url="redis://localhost:6379/0")