__all__ = ["router"]

import logging

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from ..data_gateway import UserDB
from ..data_gateway.types import User
from ..services import Authentication

logger = logging.getLogger(__name__)


class AuthRequest(BaseModel):
    username: str
    password: str


router = APIRouter(prefix="/auth", tags=["auth"])
authentication_service = Authentication(UserDB)


@router.post("/")
async def authenticate(payload: AuthRequest) -> User:
    logger.info("Auth attempt for user %s", payload.username)
    user: User = authentication_service.login(payload.username, payload.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    return user
