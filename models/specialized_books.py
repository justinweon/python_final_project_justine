from.base_book import Book

class Paperbook(Book):
    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)
        self.__pages = pages

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, 페이지수: {self.__pages}p (단행본)"


class Ebook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title,author,isbn)
        self.__file_size = file_size

    def display_info(self):
        base_info = super().display_info
        return f"{base_info}, 파일크기: {self.__file_size}MB (전자도서)"