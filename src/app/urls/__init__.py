from django.conf.urls import include
from django.contrib import admin
from django.urls import path

api = [
    path("v1/", include("app.urls.v1")),
]

urlpatterns = [
    path("api/", include(api)),
    path("admin/", admin.site.urls),
]
