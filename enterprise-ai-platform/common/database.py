"""
Async Database Infrastructure Manager
Manages SQLAlchemy 2.0 connection pool, session creation, and FastAPI dependency injection.
"""

from typing import AsyncGenerator
import logging
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

from .config import settings

logger = logging.getLogger("salesgenie.database")

# Initialize Async Engine
if settings.USE_SQLITE:
    async_engine: AsyncEngine = create_async_engine(
        settings.ASYNC_DATABASE_URL,
        echo=settings.DEBUG,
    )
else:
    async_engine: AsyncEngine = create_async_engine(
        settings.ASYNC_DATABASE_URL,
        echo=settings.DEBUG,
        pool_size=settings.DB_POOL_SIZE,
        max_overflow=settings.DB_MAX_OVERFLOW,
        pool_timeout=settings.DB_POOL_TIMEOUT,
        pool_recycle=settings.DB_POOL_RECYCLE,
        pool_pre_ping=True,
    )

# Async Session Factory
AsyncSessionFactory: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency yielding an async database session per request lifecycle.
    Ensures safe rollback on unhandled exceptions and session closure.
    """
    async with AsyncSessionFactory() as session:
        try:
            yield session
            await session.commit()
        except Exception as exc:
            await session.rollback()
            logger.error(f"Database transaction rollback due to error: {exc}", exc_info=True)
            raise
        finally:
            await session.close()
