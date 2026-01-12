from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from app.schemas.user import UserCreate, UserRead
from app.models.user import User
from app.db.session import AsyncSessionLocal

router = APIRouter(prefix="/users", tags=["users"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("", response_model=UserRead)
async def create_user(payload: UserCreate):
    async with AsyncSessionLocal() as db:
        user = User(
            email=payload.email,
            hashed_password=pwd_context.hash(payload.password)
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
