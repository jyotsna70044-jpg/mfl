from fastapi import FastAPI
from routers import users, address, loans, payments

from db.init_db import init_db

app = FastAPI(title="Loan API")


@app.on_event("startup")
async def startup():
    await init_db()


from sqlalchemy.orm import registry

print(registry().mappers)
app.include_router(users.router)
app.include_router(address.router)
app.include_router(loans.router)
app.include_router(payments.router)
