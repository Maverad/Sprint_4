import pytest
from main import BooksCollector

class TestBooksCollector():
    def test_add_new_book_add_two_books(self, collector:BooksCollector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    def test_add_new_book_name_more_than_41(self, collector:BooksCollector, books_type:dict):
        collector.add_new_book(books_type.get('more_than_41'))

        assert len(collector.books_genre) == 0

    def test_add_new_book_add_duplicate(self, collector:BooksCollector, books_type:dict):
        collector.add_new_book(books_type.get('valid'))
        collector.add_new_book(books_type.get('valid'))

        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_existing_genre(self, collector:BooksCollector, books_type:dict, genre):
        collector.add_new_book(books_type.get('valid'))
        collector.set_book_genre(name=books_type.get('valid'), genre=genre)
        
        assert collector.books_genre.get(books_type.get('valid')) == genre

    def test_set_book_genre_not_existing_genre(self, collector:BooksCollector, books_type:dict, genre_type:dict):
        collector.add_new_book(books_type.get('valid'))
        collector.set_book_genre(books_type.get('valid'), genre_type.get('invalid'))

        assert collector.books_genre.get(books_type.get('valid')) == ''

    def test_get_book_genre_existing_book(self, collector:BooksCollector, books_type:dict, genre_type:dict):
        collector.add_new_book(books_type.get('valid'))
        collector.set_book_genre(books_type.get('valid'), genre_type.get('valid'))

        assert collector.get_book_genre(books_type.get('valid')) == genre_type.get('valid')

    def test_get_book_genre_not_existing_book(self, collector:BooksCollector):
        assert collector.get_book_genre('not exist') == None

    def test_get_books_with_specific_genre_existing_genre(self, collector:BooksCollector, books_type:dict, genre_type:dict):
        collector.add_new_book(books_type.get('valid'))
        collector.set_book_genre(books_type.get('valid'), genre_type.get('valid'))
        collector.add_new_book(books_type.get('valid2'))
        collector.set_book_genre(books_type.get('valid2'), genre_type.get('valid2'))
        
        assert len(collector.get_books_with_specific_genre(genre_type.get('valid'))) == 1

    def test_get_books_with_specific_genre_not_existing_genre(self, collector:BooksCollector, books_type:dict, genre_type:dict):
        collector.add_new_book(books_type.get('valid'))
        collector.set_book_genre(books_type.get('valid'), genre_type.get('invalid'))
        
        assert len(collector.get_books_with_specific_genre(genre_type.get('invalid'))) == 0

    def test_get_books_genre_with_existing_book_and_genre(self, collector:BooksCollector, books_type:dict, genre_type:dict):
        collector.add_new_book(books_type.get('valid'))
        collector.set_book_genre(books_type.get('valid'), genre_type.get('valid'))

        assert collector.get_book_genre(books_type.get('valid')) == genre_type.get('valid')

    def test_get_books_genre_with_existing_book_and_no_genre(self, collector:BooksCollector, books_type:dict):
        collector.add_new_book(books_type.get('valid'))

        assert collector.get_books_genre() == {books_type.get('valid'): ''}

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_genre_with_age_rating(self, collector:BooksCollector, books_type:dict, genre):
        collector.add_new_book(books_type.get('valid'))
        collector.set_book_genre(books_type.get('valid'), genre)

        assert books_type.get('valid') not in collector.get_books_for_children()

    def test_add_book_in_favorites_add_books_with_duplicates(self, collector:BooksCollector, books_type:dict):
        collector.add_new_book(books_type.get('valid'))
        collector.add_book_in_favorites(books_type.get('valid'))
        collector.add_book_in_favorites(books_type.get('valid'))

        assert len(collector.favorites) == 1
    
    def test_delete_book_from_favorites_positive(self, collector:BooksCollector, books_type:dict):
        collector.add_new_book(books_type.get('valid'))
        collector.add_book_in_favorites(books_type.get('valid'))
        collector.delete_book_from_favorites(books_type.get('valid'))

        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_positive(self, collector:BooksCollector, books_type:dict, genre_type:dict):
        collector.add_new_book(books_type.get('valid'))
        collector.add_book_in_favorites(books_type.get('valid'))

        assert collector.favorites == [books_type.get('valid')]


    