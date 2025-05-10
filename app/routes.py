from advanced_alchemy.extensions.litestar import providers
from advanced_alchemy.service import OffsetPagination
from litestar import Controller, delete, get, post, put
from litestar.status_codes import HTTP_204_NO_CONTENT

from app.schemas import UserReturn, UserSchema
from app.service import UserService


class UserController(Controller):
    path = '/users'

    dependencies = providers.create_service_dependencies(UserService, 'user_service')

    @post()
    async def create_user(self, user_service: UserService, data: UserSchema) -> UserReturn:
        user = await user_service.create(data, auto_commit=True)
        return user_service.to_schema(user, schema_type=UserReturn)

    @get()
    async def list_users(self, user_service: UserService) -> OffsetPagination[UserReturn]:
        users = await user_service.list()
        return user_service.to_schema(users, schema_type=UserReturn)

    @get('/{user_id:int}')
    async def get_user(self, user_id: int, user_service: UserService) -> UserReturn:
        user = await user_service.get_one(id=user_id)
        return user_service.to_schema(user, schema_type=UserReturn)

    @put('/{user_id:int}')
    async def update_user(self, user_id: int, data: UserSchema, user_service: UserService) -> UserSchema:
        user = await user_service.update(data, item_id=user_id, auto_commit=True)
        return user_service.to_schema(user, schema_type=UserSchema)

    @delete('/{user_id:int}', status_code=HTTP_204_NO_CONTENT)
    async def delete_user(self, user_id: int, user_service: UserService) -> None:
        await user_service.delete(user_id, auto_commit=True)
