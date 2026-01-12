# from typing import Optional, List
#
#
# class AddressCreate(BaseModel):
#     line1: str
#     line2: Optional[str] = None
#     city: str
#     state: str
#     postal_code: str
#     country: str
#
#
# class AddressRead(AddressCreate):
#     id: int
#     model_config = ConfigDict(from_attributes=True)


from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: int
    email: EmailStr
    role: str

    model_config = {"from_attributes": True}
