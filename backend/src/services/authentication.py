__all__ = ["Authentication", "Token"]

from dataclasses import dataclass

from ..data_gateway import DataGateway
from ..data_gateway.types import UserNotFoundError
from ..data_gateway.types.user import User as UserDB
from ..utils.jwt_utils import encode_jwt


@dataclass(frozen=True)
class User:
    id: int
    username: str


@dataclass(frozen=True)
class Token:
    token: str
    user: User


class Authentication:
    def __init__(self, db: DataGateway):
        self.db = db

    def login(self, username: str, password: str) -> Token:
        """
        Raises:
            UserNotFoundError: If the user does not exist.
        """
        user: UserDB = self.db.User.get_user_by_username(username)
        if user.password != password:
            raise UserNotFoundError()
        return Token(
            token=encode_jwt(user.to_dict()),
            user=User(id=user.id, username=user.username),
        )
