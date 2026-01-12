from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import pool
from logging.config import fileConfig
from alembic import context
from app.db.session import Base
from app.core.config import settings

config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_online():
    connectable = async_engine_from_config(
        {
            "sqlalchemy.url": settings.DATABASE_URL,
        },
        poolclass=pool.NullPool,
    )

    async def run_async_migrations():
        async with connectable.connect() as connection:
            await connection.run_sync(
                context.configure,
                connection=connection,
                target_metadata=target_metadata,
            )

            with context.begin_transaction():
                context.run_migrations()

    import asyncio
    asyncio.run(run_async_migrations())


run_migrations_online()
