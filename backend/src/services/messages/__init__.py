__all__ = ["MessagesService"]

from ...data_gateway import DataGateway
from ...data_gateway.types.message import WebhookMessage as RawWebhookMessage


class MessagesService:
    def __init__(self, db: DataGateway):
        self.db = db

    def push(self, dto_message: RawWebhookMessage):
        self.db.Message.push_message(dto_message)

    def get_messages(self) -> list[RawWebhookMessage]:
        return self.db.Message.get_messages()
