from fastapi import FastAPI
from app.routers import auth, users, loans, payments


app = FastAPI(title="Loan API")


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(loans.router)
app.include_router(payments.router)