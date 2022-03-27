from typing import Optional

from dataclasses import dataclass
from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    email = serializers.EmailField()
    username = serializers.CharField(max_length=128, read_only=True)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "username"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


@dataclass
class UserCreator:
    """
    Create a new user, raise an error if a user with specified email already exists
    """

    email: str
    password: str

    def __call__(self) -> User:
        self._check_if_user_already_exists()
        return self._create_user()

    def _create_user(self) -> User:
        serializer = UserSerializer(
            data={"email": self.email, "password": self.password}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.instance

    def _check_if_user_already_exists(self) -> None:
        if User.objects.filter(email=self.email).exists():
            raise ValueError
