# alembic/env.py
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from src.infrastructure.config.settings import settings
from src.infrastructure.database.models.user_model import Base

config = context.config
config.set_main_option('sqlalchemy.url', settings.DATABASE_URL)
connectable = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix='sqlalchemy.',
    poolclass=pool.NullPool)

fileConfig(config.config_file_name)

with connectable.connect() as connection:
    context.configure(
        connection=connection,
        target_metadata=Base.metadata
    )

    with context.begin_transaction():
        context.run_migrations()