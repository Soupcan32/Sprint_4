import pytest
from main import BooksCollector


@pytest.fixture
def collector()->BooksCollector:
    return BooksCollector()

class TestBooksCollector:

    def test_add_new_book_add_two_books(self,collector:BooksCollector):
        collector.add_new_book('Тестовая книга')
        collector.add_new_book('Тестовая книга 2')
        assert len(collector.get_books_genre())==2
    
    @pytest.mark.parametrize('name',['', 'К' * 41, 'К' * 50])
    def test_add_new_book_invalid_name_length_book_not_added(self,collector:BooksCollector,name):
        collector.add_new_book(name)
        assert collector.get_books_genre()=={}

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_existing_genre_genre_set(self,collector:BooksCollector,genre):
        collector.add_new_book('Тестовая книга 3')
        collector.set_book_genre('Тестовая книга 3',genre)
        assert collector.get_books_genre()['Тестовая книга 3'] == genre

    def test_get_book_genre_book_with_genre_returns_genre(self, collector: BooksCollector):
        collector.add_new_book('Тестовая книга 4')
        collector.set_book_genre('Тестовая книга 4','Фантастика')
        assert collector.get_book_genre('Тестовая книга 4') == 'Фантастика'    

    def test_get_books_with_specific_genre_returns_only_books_of_this_genre(self, collector: BooksCollector):
        books = {'Дюна': 'Фантастика', 'Оно': 'Ужасы', 'Солярис': 'Фантастика'}
        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна', 'Солярис']

    def test_get_books_genre_returns_dict_with_books_and_genres(self, collector: BooksCollector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Оно')
        assert collector.get_books_genre() == {'Дюна': 'Фантастика', 'Оно': ''}        

    @pytest.mark.parametrize('genre, expected', [
        ('Фантастика', ['Книга']),
        ('Мультфильмы', ['Книга']),
        ('Комедии', ['Книга']),
        ('Ужасы', []),
        ('Детективы', []),
    ])
    def test_get_books_for_children_only_genres_without_age_rating(self, collector: BooksCollector, genre, expected):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', genre)
        assert collector.get_books_for_children() == expected    

    def test_add_book_in_favorites_same_book_twice_added_once(self, collector: BooksCollector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert collector.favorites == ['Дюна']    

    def test_delete_book_from_favorites_book_in_favorites_deleted(self, collector: BooksCollector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert collector.favorites == []  
          
    def test_get_list_of_favorites_books_returns_all_favorites(self, collector: BooksCollector):
        for name in ['Дюна', 'Оно']:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == ['Дюна', 'Оно']    