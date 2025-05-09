from advanced_alchemy.exceptions import NotFoundError
from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin
from litestar_granian import GranianPlugin

from app.db import alchemy_plugin
from app.exception_handlers import not_found_handler
from app.routes import UserController

app = Litestar(
    plugins=[
        alchemy_plugin,
        GranianPlugin(),
    ],
    debug=True,
    route_handlers=[UserController],
    openapi_config=OpenAPIConfig(
        title='litestar-project',
        description='REST API для управления пользователями',
        version='0.1.0',
        render_plugins=[SwaggerRenderPlugin()],
    ),
    exception_handlers={
        NotFoundError: not_found_handler,
    },
)
