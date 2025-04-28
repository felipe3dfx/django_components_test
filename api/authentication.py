from user.models import User


def user_authentication_rule(user: User) -> bool:
    """User authentication rule."""
    return bool(user is not None and user.is_active)
