__all__ = ["Authentication"]

from ..data_gateway import DataGateway
from ..data_gateway.types import User


class Authentication:
    def __init__(self, db: DataGateway):
        self.db = db

    def login(self, username: str, password: str) -> User:
        return self.db.User.check_auth(username, password)
