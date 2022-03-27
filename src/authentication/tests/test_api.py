import pytest
from rest_framework.test import APIClient

from authentication.models import User

pytestmark = [
    pytest.mark.django_db,
]
api_client = APIClient()


def test_register_user():
    response = api_client.post(
        "/api/v1/register/",
        {"email": "test@example.com", "password": "user.password"},
    )
    assert response.status_code == 201
    assert response.data["username"] == "test@example.com"
    assert response.data["email"] == "test@example.com"


def test_register_with_duplicated_email():
    user = User.objects.create_user(email="admin@example.com", password="Aq1Sw2De3")
    response = api_client.post(
        "/api/v1/register/",
        {"email": user.email, "password": user.password},
    )
    assert response.status_code == 400
    assert response.data["detail"] == "Email is already used."


def test_register_user_without_password():
    response = api_client.post(
        "/api/v1/register/",
        {"email": "test+1@example.com"},
    )
    assert response.status_code == 400
    assert response.data["password"][0] == "This field may not be null."


def test_register_user_without_email():
    response = api_client.post(
        "/api/v1/register/",
        {"password": "user.password"},
    )
    assert response.status_code == 400
    assert response.data["email"][0] == "This field may not be null."


def test_register_user_with_not_valid_email():
    response = api_client.post(
        "/api/v1/register/",
        {"email": "user", "password": "Aq1Sw2De3"},
    )
    assert response.status_code == 400
    assert response.data["email"][0] == "Enter a valid email address."


def test_register_user_with_short_password():
    response = api_client.post(
        "/api/v1/register/",
        {"email": "user", "password": "Aq1"},
    )
    assert response.status_code == 400
    assert (
        response.data["password"][0] == "Ensure this field has at least 8 characters."
    )
