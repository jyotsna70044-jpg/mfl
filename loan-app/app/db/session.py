# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
# from app.core.config import settings
#
# engine = create_async_engine(
#     settings.DATABASE_URL,
#     pool_size=10,
#     max_overflow=20,
#     pool_pre_ping=True,
# )
#
# AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
    future=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)

class Base(DeclarativeBase):
    pass

