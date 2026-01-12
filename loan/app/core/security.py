from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(subject: str, role: str):
    payload = {
        "sub": subject,
        "role": role,
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
