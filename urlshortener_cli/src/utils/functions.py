import os
import secrets
import string
import time



def get_current_time() -> float:
    return time.time()


def create_random_key(length: int = 5) -> str:
    #TODO improve with uuid
    chars = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))


def is_expired(url_time: float) -> bool:
    now = get_current_time()
    limit = os.getenv('EXIPRATION_TIME')

    return now - url_time > float(limit)
