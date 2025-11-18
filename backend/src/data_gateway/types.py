__all__ = ["MessageStore", "UsersStore", "DataGateway"]


from typing import Protocol, runtime_checkable

from ..entities import User, WebhookMessage


@runtime_checkable
class MessageStore(Protocol):
    @classmethod
    def push_message(cls, message: WebhookMessage) -> None: ...

    @classmethod
    def get_messages(cls) -> list[WebhookMessage]: ...


@runtime_checkable
class UsersStore(Protocol):
    @classmethod
    def check_auth(cls, username: str, password: str) -> User: ...


@runtime_checkable
class DataGateway(Protocol):
    Message: MessageStore
    User: UsersStore
