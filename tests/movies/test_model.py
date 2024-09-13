import pytest

from movies.models import Movie

@pytest.mark.django_db
def test_movie_model():
    assert 1 == 1