from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from passlib.context import CryptContext
from app.db.session import AsyncSessionLocal
from app.models.user import User
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/login")
async def login(email: str, password: str):
    async with AsyncSessionLocal() as db:
        q = await db.execute(select(User).where(User.email == email))
        user = q.scalar_one_or_none()
        if not user or not pwd_context.verify(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"access_token": create_access_token(str(user.id), user.role)}
