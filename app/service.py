from typing import Any

from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from passlib.hash import bcrypt

from app.models import User


class UserService(SQLAlchemyAsyncRepositoryService[User]):
    class Repo(SQLAlchemyAsyncRepository[User]):
        model_type = User

    repository_type = Repo

    async def create(self, data, **kwargs) -> User:
        data.password = bcrypt.hash(data.password)
        return await super().create(data=data, **kwargs)

    async def update(self, data, item_id: Any | None = None, **kwargs) -> User:
        data.password = bcrypt.hash(data.password)
        return await super().update(data=data, item_id=item_id, **kwargs)
