from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    User,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str) -> User:
        """Create and return a `User` with an email and password."""

        user = self.model(username=email, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email: str, password: str) -> User:
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        user = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    def __str__(self) -> str:
        """
        Returns a string representation of this `User`.
        """
        return self.email

    def get_full_name(self) -> str:
        """
        This method is required by Django for things like handling emails.
        """
        return self.username

    def get_short_name(self) -> str:
        """
        This method is required by Django for things like handling emails.
        """
        return self.username
