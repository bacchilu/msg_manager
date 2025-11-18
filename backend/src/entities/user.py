__all__ = ["User"]

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    username: str
    password: str
