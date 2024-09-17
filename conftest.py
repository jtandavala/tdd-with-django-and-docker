# import os
# from django.conf import settings

# import pytest

# DEFAULT_ENGINE = "django.db.backends.sqlite3"


# @pytest.fixture(scope="session")
# def django_db_setup():
#     settings.DATABASES["default"] = {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.environ.get("POSTGRES_DB"),
#         "USER": os.environ["POSTGRES_USER"],
#         "PASSWORD": os.environ["POSTGRES_PASSWORD"],
#         "HOST": os.environ["POSTGRES_HOST"],
#         "PORT": "5432",
#         "ATOMIC_REQUESTS": True,
#     }

# contest.py

import os

from django.conf import settings

import pytest


DEFAULT_ENGINE = "django.db.backends.sqlite3"





