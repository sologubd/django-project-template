from rest_framework.exceptions import APIException


class UserExistsAPIException(APIException):
    status_code = 400
    default_detail = "Email is already used."
    default_code = "email_is_used"
