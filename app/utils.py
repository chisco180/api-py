from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


pwd_context = PasswordHasher()


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):

    try:
        return pwd_context.verify(hashed_password, plain_password)
    except VerifyMismatchError:
        return False
