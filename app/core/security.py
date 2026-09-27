from datetime import datetime, timedelta, timezone

from jose import jwt
from pwdlib import PasswordHash

SECRET_KEY = "change-this-secret-later"
ALGORITHM = "HS256"

password_hash = PasswordHash.recommended()


def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def create_access_token(user_id: int):
    expire = datetime.now(timezone.utc) + timedelta(hours=1)

    payload = {
        "sub": str(user_id),
        "exp": expire,
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)