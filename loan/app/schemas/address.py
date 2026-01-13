from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict


class AddressCreate(BaseModel):
    user_id: int
    muhalla: str
    ward_no: str
    village: str
    post_office: str
    police_station: str
    postal_code: str
    district: str
    state: str
    country: str


class AddressRead(AddressCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
    # model_config = {"from_attributes": True}
