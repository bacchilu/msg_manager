__all__ = ["RawUser"]

from dataclasses import dataclass


@dataclass(frozen=True)
class RawUser:
    id: int
    username: str
    password: str

    def to_dict(self) -> dict[str, str | int]:
        return {"id": self.id, "username": self.username}
