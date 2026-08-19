from models.specialized_books import Paperbook, Ebook
from utils.helpers import get_string, get_valid_integer, get_valid_float

def main():
    book_catalogue = {}
    isbn_set = set()

    while True:
        print("/n"+"="*30)
        print ("도서관리시스템")
        print ("="*30)
        print ('1. 도서 등록')
        print ("2. 전체 도서 조회")
        print ("3. 도서 검색")
        print ("4. 대여/반납 처리")
        print ("5. 종료")
        print ("="*30)

        choice = get_valid_integer("메뉴를 선책하세요(1-5)", "문자나 공백이 아닌 숫자 (1~5)만 입력하세요.")

        if choice == 1:
            print ("[1. 도서등록]")

            title = get_string("도서명: ")
            author = get_string("저자: ")
            isbn = get_string ("ISBN: ")

            if isbn in isbn_set:
                print(f"이미 등록된 ISBN({isbn})입니다.")
                continue

            book_type = get_string("도서 종류를 선택하세요 (1: 단행본, 2: 전자도서)")

            if book_type =='1':
                pages = get_valid_integer("페이지 수:", "페이지 수는 숫자로입력하세요.")
                new_book = Paperbook(title, author, isbn, pages)

            elif book_type == '2':
                file_size = get_valid_float("파일크기(MB):", "파일 크기는 숫자로 입력해야 합니다.")
                new_book = Ebook(title,author,isbn,file_size)

            else:
                print("올바른 도서 종류(1 또는 2)를 선택해주세요")
                continue

            #도서추가
            book_catalogue[isbn] = new_book
            isbn_set.add(isbn)
            print(f"도서가 등록되었습니다 - {title}")
        elif choice == 2:
            print("2. 전체 도서 조회")
            if not book_catalogue:
                print ("등록된 도서가 없습니다")

            else:
                for book in book_catalogue.values():
                    print(book.display_info())
        elif choice == 3:
            print("3. 도서검색")
            keyword = get_string("검색할 도서명을 입력하세요:")

            found = False
            for book in book_catalogue.values():
                if keyword in book.get_title():
                    print(book.display_info())
                    found = True

        elif choice == 4:
            print ("4. 대여/반납 처리")

            target_isbn = get_string("처리할 도서의 ISBN을 입력하세요:")
            if target_isbn not in book_catalogue:
                print ("해당 ISBN을 가진 도서를 찾을 수 없습니다.")
            else:
                target_book = book_catalogue[target_isbn]

                if target_book.is_borrowed():
                    target_book.set_borrow_status(False)
                    print(f"도서가 반납되었습니다 - {target_book.get_title()}")
                else:
                    target_isbn.set_borrow_status(True)
                    print(f"도서가 대여되었습니다 - {target_book.get.title}")

        elif choice == 5:
            print("프로그램을 종료합니다. 감사합니다.")
            break

        else:
            print ("1~5 사이의 메뉴 번호를 선택하세요.")


if __name__ =="__main__":
    print(main())