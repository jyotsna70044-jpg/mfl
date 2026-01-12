from fastapi import FastAPI
from routers import loans
from db.session import engine
from db.base import Base


app = FastAPI(title="Loan API")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(loans.router)
