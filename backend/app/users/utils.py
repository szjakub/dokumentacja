import secrets
from hashlib import shake_256
from django.contrib.auth import get_user_model

User = get_user_model()


def username_generator(first_name: str, last_name: str) -> str:
    prefix = first_name[0].lower() + last_name[0].lower()
    postfix = secrets.token_hex(4)
    used_usernames = User.objects.all().values_list('username', flat=True)
    while prefix + postfix in used_usernames:
        postfix = secrets.token_hex(4)
    return prefix + postfix


def password_generator() -> str:
    random_key = secrets.token_hex(20)
    return shake_256(random_key.encode()).hexdigest(10)
