from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, **kwargs):  # noqa: FBT002
        user = self.model(
            email=UserManager.normalize_email(email),
            is_active=is_active,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
