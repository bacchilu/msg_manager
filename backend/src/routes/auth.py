__all__ = ["router"]

import logging

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from ..data_gateway import MockDB
from ..data_gateway.types import UserNotFoundError
from ..services import Authentication, Token

logger = logging.getLogger(__name__)


class AuthRequest(BaseModel):
    username: str
    password: str


router = APIRouter(prefix="/auth", tags=["auth"])
authentication_service = Authentication(MockDB())


@router.post("/")
async def authenticate(payload: AuthRequest) -> Token:
    logger.info("Auth attempt for user %s", payload.username)
    try:
        return authentication_service.login(payload.username, payload.password)
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
