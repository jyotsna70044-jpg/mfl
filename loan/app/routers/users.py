from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from core.security import hash_password
from schemas.user import UserCreate, UserRead
from models.user import User
from db.session import AsyncSessionLocal

router = APIRouter(prefix="/users", tags=["users"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



@router.post("", response_model=UserRead)
async def create_user(payload: UserCreate):
    # hashed_password = pwd_context.hash(payload.password),
    async with AsyncSessionLocal() as db:
        user = User(
            email=payload.email,
            hashed_password=hash_password(payload.password),
            mobile=payload.mobile
        )
        print(user)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
