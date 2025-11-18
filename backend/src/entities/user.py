__all__ = ["User"]

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    username: str
    password: str

    def to_dict(self):
        return {"id": self.id, "username": self.username}
