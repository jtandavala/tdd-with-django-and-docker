import pytest
from django.conf import settings

from movies.models import Movie



@pytest.mark.django_db
def test_make_sure_to_use_sqlite3():
    assert settings.DATABASES["default"]["ENGINE"] == "django.db.backends.sqlite3"

