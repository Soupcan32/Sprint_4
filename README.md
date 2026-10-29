# Sprint_4

- `test_add_new_book_add_two_books` - тест проверяет, что при добавлении двух книг в словаре оказывается ровно 2 книги.
- `test_add_new_book_invalid_name_length_book_not_added` - тест проверяет, что книга с названием недопустимой длины (0, 41 и 50 символов) не добавляется.
- `test_set_book_genre_existing_genre_genre_set` - тест проверяет, что книге устанавливается любой жанр из списка доступных.
- `test_get_book_genre_book_with_genre_returns_genre` -тест проверяет, что метод возвращает жанр книги по её названию.
- `test_get_books_with_specific_genre_returns_only_books_of_this_genre` - тест проверяет, что метод возвращает только книги указанного жанра.
- `test_get_books_genre_returns_dict_with_books_and_genres` - тест проверяет, что метод возвращает словарь со всеми книгами и их жанрами.
- `test_get_books_for_children_only_genres_without_age_rating` - тест проверяет, что в список для детей попадают только книги жанров без возрастного рейтинга.
- `test_add_book_in_favorites_same_book_twice_added_once` - тест проверяет, что одна и та же книга добавляется в избранное только один раз.
- `test_delete_book_from_favorites_book_in_favorites_deleted` -тест проверяет, что книга удаляется из избранного.
- `test_get_list_of_favorites_books_returns_all_favorites` - тест проверяет, что метод возвращает все книги из избранного.
