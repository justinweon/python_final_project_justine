class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_borrowed = False 

def get_isbn(self):
    return self.__isbn

def get_title(self):
    return self.__title

def get_author(self):
    return self.__author

def is_borrowed(self):
    self.__is_borrowed = status

def display_info(self):
    status = "대여중" if self.__is_borrowed else "대여가능"

    return f"[{status}] 제목 : {self.__title}, 저자 : {self.__author}, ISBN : {self.__isbn}"