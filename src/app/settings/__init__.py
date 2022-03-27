from pathlib import Path
from split_settings.tools import include

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True
STATIC_URL = "static/"
ROOT_URLCONF = "app.urls"
WSGI_APPLICATION = "app.wsgi.application"

include(
    "config/base.py",
    "config/database.py",
    "config/drf.py",
    "config/installed_apps.py",
    "config/middlewares.py",
    "config/security.py",
)
