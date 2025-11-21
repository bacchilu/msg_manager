"""Protocols defining the gateway interfaces for users and messages."""

__all__ = ["MessageStore", "UsersStore", "DataGateway", "UserNotFoundError"]

from typing import Protocol, runtime_checkable

from .message import WebhookMessage
from .user import User


class UserNotFoundError(Exception):
    pass


@runtime_checkable
class MessageStore(Protocol):
    @classmethod
    def push_message(cls, message: WebhookMessage) -> None: ...

    @classmethod
    def get_messages(cls) -> list[WebhookMessage]: ...


@runtime_checkable
class UsersStore(Protocol):
    @classmethod
    def get_user_by_username(cls, username: str) -> User:
        """
        Looks up a user by username.

        Raises:
            UserNotFoundError: If the user does not exist.
        """
        ...


@runtime_checkable
class DataGateway(Protocol):
    Message: MessageStore
    User: UsersStore
