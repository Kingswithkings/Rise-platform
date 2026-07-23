from app.users.models import User


def is_admin(user: User) -> bool:
    return bool(user.is_admin)
