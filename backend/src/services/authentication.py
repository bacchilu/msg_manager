__all__ = ["Authentication"]

from ..data_gateway import UsersStore
from ..data_gateway.types import User


class Authentication:
    def __init__(self, db: UsersStore):
        self.db = db

    def login(self, username: str, password: str) -> User:
        return self.db.check_auth(username, password)
