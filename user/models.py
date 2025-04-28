from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('first_name', 'last_name')

    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=128,
    )

    last_name = models.CharField(
        max_length=128,
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name='staff',
    )

    is_active = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f'{self.get_full_name} <{self.email}>'

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
