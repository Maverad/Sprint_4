import pytest
from main import BooksCollector


@pytest.fixture
def collector() -> BooksCollector:
    collector = BooksCollector()
    return collector

@pytest.fixture
def books_type() -> dict:
    books = {
        'valid':'Война и мир', 
        'valid2': 'Мертвые души',
        'more_than_41': 'Ооооооооооочччччееееееннь большое название',
        'empty': '',
        'wrong_type': 123
        }
    return books

@pytest.fixture
def genre_type() -> dict:
    genre = {
        'valid': 'Фантастика',
        'valid2': 'Мультфильмы',
        'invalid': 'Артхаус',
        'age_rating': 'Ужасы'
    }
    return genre
