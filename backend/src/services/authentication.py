__all__ = ["Authentication"]

from ..data_gateway import DataGateway
from ..data_gateway.types import User, UserNotFoundError


class Authentication:
    def __init__(self, db: DataGateway):
        self.db = db

    def login(self, username: str, password: str) -> User:
        """
        Raises:
            UserNotFoundError: If the user does not exist.
        """
        user: User = self.db.User.get_user_by_username(username)
        if user.password != password:
            raise UserNotFoundError()
        return user
