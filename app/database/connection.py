from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from sqlalchemy.orm import declarative_base


DATABASE_URL = "postgresql+asyncpg://fastapi_user:fastapi_pass@localhost:5432/fastapi_async"


engine = create_async_engine(
    DATABASE_URL
)


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


Base = declarative_base()