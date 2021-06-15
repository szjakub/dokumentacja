from hashlib import shake_256


def username_generator(data: str) -> str:
    return shake_256(data.encode()).hexdigest(5)


def password_generator(data: str) -> str:
    return shake_256(data.encode()).hexdigest(10)
