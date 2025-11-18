__all__ = ["encode_jwt", "decode_jwt"]

from datetime import datetime, timedelta, timezone
from typing import Any

import jwt

SECRET: str = "Salve, mondo!"
ALGORITHM: str = "HS256"


def encode_jwt(payload: dict[str, Any]) -> str:
    EXP: datetime = datetime.now(timezone.utc) + timedelta(hours=24)

    return jwt.encode({**payload, "exp": EXP}, SECRET, algorithm=ALGORITHM)


def decode_jwt(token: str) -> dict[str, Any]:
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    except jwt.InvalidTokenError as exc:
        raise Exception() from exc
