from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.exceptions import UserExistsAPIException
from authentication.services.user_creator import UserCreator


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        registration_data = {
            "email": request.data.get("email"),
            "password": request.data.get("password"),
        }

        try:
            create_user = UserCreator(**registration_data)
            user = create_user()
        except ValueError:
            raise UserExistsAPIException

        return Response(
            {"email": user.email, "username": user.email},
            status=status.HTTP_201_CREATED,
        )
