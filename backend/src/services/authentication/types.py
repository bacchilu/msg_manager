__all__ = ["User", "Token"]

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    username: str


@dataclass(frozen=True)
class Token:
    token: str
    user: User
