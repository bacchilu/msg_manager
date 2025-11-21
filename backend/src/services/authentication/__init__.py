__all__ = ["Authentication", "Token"]

from ...data_gateway import DataGateway
from ...data_gateway.types import UserNotFoundError
from ...data_gateway.types.user import RawUser
from ...utils.jwt_utils import encode_jwt
from .types import Token, User


class Authentication:
    def __init__(self, db: DataGateway):
        self.db = db

    def login(self, username: str, password: str) -> Token:
        """
        Raises:
            UserNotFoundError: If the user does not exist.
        """
        user: RawUser = self.db.User.get_user_by_username(username)
        if user.password != password:
            raise UserNotFoundError()
        return Token(
            token=encode_jwt(user.to_dict()),
            user=User(id=user.id, username=user.username),
        )
