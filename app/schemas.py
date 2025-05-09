from msgspec import Struct


class UserSchema(Struct):
    name: str
    surname: str
    password: str


class UserReturn(Struct):
    id: int
    name: str
    surname: str
