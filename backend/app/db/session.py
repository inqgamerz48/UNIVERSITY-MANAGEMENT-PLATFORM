from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# For Async, we need `postgresql+asyncpg` driver in connection string usually, 
# or use strict asyncpg. But for simplicity in dev without complex setup, 
# ensuring the URL structure is correct:
# If DATABASE_URL is "postgresql://...", we might need to modify it to "postgresql+asyncpg://..."
DB_URL = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

engine = create_async_engine(DB_URL, echo=True, future=True)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
