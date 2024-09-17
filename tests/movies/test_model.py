import pytest
from django.conf import settings

from movies.models import Movie



@pytest.mark.django_db
def test_make_sure_to_use_sqlite3():
    assert settings.DATABASES["default"]["ENGINE"] == "django.db.backends.sqlite3"


@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title="Raising Arizona", genre="comedy", year="1987")
    movie.save()

    assert movie.title == "Raising Arizona"
    assert movie.genre == "comedy"
    assert movie.year == "1987"
    assert movie.created_date
    assert movie.updated_date
    assert str(movie) == movie.title



