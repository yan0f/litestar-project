from advanced_alchemy.extensions.litestar import SQLAlchemyAsyncConfig, SQLAlchemyPlugin

from app.config import DATABASE_URL

alchemy_config = SQLAlchemyAsyncConfig(connection_string=DATABASE_URL)
alchemy_plugin = SQLAlchemyPlugin(config=alchemy_config)
