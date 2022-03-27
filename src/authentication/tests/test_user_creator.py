import pytest
from collections import namedtuple

from authentication.models import User
from authentication.services.user_creator import UserCreator

pytestmark = [
    pytest.mark.django_db,
]


@pytest.fixture
def user_obj():
    UserObj = namedtuple("UserObj", ("email", "password"))
    return UserObj("test@example.com", "AQ1Sw2De3")


@pytest.fixture
def user(user_obj):
    create_user = UserCreator(user_obj.email, user_obj.password)
    return create_user()


def tests_create_superuser(user_obj):
    new_user = User.objects.create_superuser(user_obj.email, user_obj.password)
    assert new_user.is_superuser is True


def tests_create_user(user_obj):
    create_user = UserCreator(user_obj.email, user_obj.password)
    new_user = create_user()
    assert new_user.get_full_name() == user_obj.email
    assert new_user.get_short_name() == user_obj.email
    assert str(new_user) == user_obj.email


def tests_create_fails_if_email_is_used(user, user_obj):
    create_user = UserCreator(user_obj.email, user_obj.password)

    assert user
    with pytest.raises(ValueError):
        create_user()
