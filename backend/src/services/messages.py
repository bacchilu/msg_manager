__all__ = ["MessagesService"]


from ..data_gateway import DataGateway
from ..data_gateway.types.message import WebhookMessage

DB: list[WebhookMessage] = []


class MessagesService:
    def __init__(self, db: DataGateway):
        self.db = db

    def push(self, dto_message: WebhookMessage):
        self.db.Message.push_message(dto_message)

    def get_messages(self) -> list[WebhookMessage]:
        return self.db.Message.get_messages()
