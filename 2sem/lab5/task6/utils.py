import hashlib
import re


def hash_password(password: str) -> str:
    # хэширование через sha256
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    return True
