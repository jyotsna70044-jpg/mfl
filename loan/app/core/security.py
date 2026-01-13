from datetime import datetime, timedelta
import hashlib
import bcrypt
from jose import jwt
from passlib.context import CryptContext
from core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(subject: str, role: str):
    payload = {
        "sub": subject,
        "role": role,
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def hash_password(password: str) -> str:
    # Step 1: SHA-256 (removes length limit)
    sha = hashlib.sha256(password.encode("utf-8")).digest()

    # Step 2: bcrypt
    hashed = bcrypt.hashpw(sha, bcrypt.gensalt())

    return hashed.decode("utf-8")


def verify_password(password: str, hashed: str) -> bool:
    sha = hashlib.sha256(password.encode("utf-8")).digest()
    return bcrypt.checkpw(sha, hashed.encode("utf-8"))
