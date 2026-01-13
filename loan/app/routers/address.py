from fastapi import APIRouter, Depends

from schemas.address import AddressCreate, AddressRead
from models.address import Address
from db.session import AsyncSessionLocal

router = APIRouter(prefix="/address", tags=["address"])


@router.post("", response_model=AddressRead)
async def create_user(payload: AddressCreate):
    async with AsyncSessionLocal() as db:
        address = Address(**payload.model_dump())
        db.add(address)
        await db.commit()
        await db.refresh(address)
        return address
