# =========================================================
# Node 클래스
# =========================================================
class Node:
    """
    1. 단순 연결 구조를 위한 Node 클래스
    2. 각 노드는 데이터 필드(data)와 다음 노드를 가리키는 링크 필드(link)를 가짐
    3. data 필드에는 Book 객체가 저장됨
    """
    def __init__(self, elem, next=None):
        # 시간 복잡도: O(1)
        self.data = elem  # 데이터 필드 (Book 객체 저장)
        self.link = next  # 다음 노드를 가리키는 링크 필드

    def append(self, new):  # 현재 노드 다음에 new 노드를 삽입
        # 시간 복잡도: O(1)
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):  # 현재 노드의 다음 노드를 삭제한 후 반환
        # 시간 복잡도: O(1)
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node

# =========================================================
# Book 클래스
# =========================================================
class Book:
    """
    1. 도서 객체의 정보를 저장하는 클래스
    2. 책 번호(book_id), 책 제목(title), 저자(author), 출판 연도(year)를 포함
    """
    def __init__(self, book_id, title, author, year):
        # 시간 복잡도: O(1)
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # 시간 복잡도: O(1)
        return f"[책 번호: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}]"

# =========================================================
# LinkedList 클래스
# =========================================================
class LinkedList:
    """
    1. 단순 연결 리스트 클래스
    2. 시간 복잡도 분석에서의 'n'은 리스트의 노드(도서) 개수를 의미합니다.
    """
    def __init__(self):
        # 시간 복잡도: O(1)
        self.head = None  # 리스트의 첫 번째 노드를 가리키는 포인터

    def isEmpty(self):
        # 시간 복잡도: O(1)
        return self.head == None  # 리스트가 비어있는지 확인

    def getNode(self, pos):
        # pos 위치의 노드를 반환
        # 시간 복잡도: O(n)
        if pos < 0: return None
        ptr = self.head
        for _ in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr

    def insert(self, pos, elem):
        # 시간 복잡도: O(n)
        new_node = Node(elem)  # 1. 새 노드 생성 (elem은 Book 객체)
        before = self.getNode(pos - 1) # 2. pos-1 노드 탐색 (O(n) 연산)
       
        if before is None:
           if pos == 0: # 머리 노드로 삽입 / O(1) 케이스
               new_node.link = self.head
               self.head = new_node
               return
           else: 
               raise IndexError("삽입할 위치가 유효하지 않음!")
        else: # 중간 노드로 삽입 / O(n) 케이스 (getNode 이후)
            before.append(new_node) # <--- O(1) 연산
        
    def delete(self, pos):
        # 시간 복잡도: O(n)
        if pos < 0:
            raise ValueError("잘못된 위치 값!")
        
        before = self.getNode(pos - 1) # <--- O(n) 연산
        
        if before == None:
            if pos == 0: # 머리 노드 삭제 / O(1) 케이스
                deleted = self.head
                if self.head is not None:
                    self.head = self.head.link
                    deleted.link = None
                return deleted
            else: 
                raise IndexError("삭제할 위치가 유효하지 않음!")
        else:  # 중간 노드 삭제 / O(n) 케이스 (getNode 이후)
            return before.popNext() # <--- O(1) 연산
        
    def size(self):
        # 리스트의 전체 노드의 개수
        # 시간 복잡도: O(n)
        ptr = self.head
        count = 0
        while ptr is not None:
            count += 1
            ptr = ptr.link
        return count
        
    def display(self, msg=""):
        # 리스트의 내용을 출력 (Book 객체용으로 수정) / 시간 복잡도: O(n)
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data) # Book 객체의 __str__ 메서드가 호출됨
            ptr = ptr.link

    # 책 제목으로 리스트에서 도서(Book 객체)를 찾기
    def find_by_title(self, title):
        # 시간 복잡도: O(n)
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return ptr.data  # Book 객체 반환
            ptr = ptr.link
        return None  # 찾지 못한 경우

    # 책 제목으로 리스트에서 도서의 위치(인덱스)를 찾기
    def find_pos_by_title(self, title):
        # 시간 복잡도: O(n)
        ptr = self.head
        pos = 0
        while ptr is not None:
            if ptr.data.title == title:
                return pos  # 위치(인덱스) 반환
            ptr = ptr.link
            pos += 1
        return -1 # 찾지 못한 경우

    # 책 번호로 리스트에서 도서(Book 객체)를 찾기 (중복 검사용)
    def find_by_id(self, book_id):
        # 시간 복잡도: O(n)
        ptr = self.head
        while ptr is not None:
            if ptr.data.book_id == book_id:
                return ptr.data # Book 객체 반환
            ptr = ptr.link
        return None # 찾지 못한 경우

# =========================================================
# BookManagement 클래스
# =========================================================
class BookManagement:
    """
    1. 도서 관리 프로그램의 메인 로직 담당 클래스
    2. LinkedList 객체를 멤버로 가짐
    3. 사용자 인터페이스(메뉴) 및 기능 실행
    4. 시간 복잡도 분석에서의 'n'은 book_list(LinkedList)의 노드 개수를 의미합니다.
    """
    def __init__(self):
        # 시간 복잡도: O(1)
        self.book_list = LinkedList() # 도서(Book 객체)를 저장할 연결 리스트

    # 1. 도서 추가 기능
    def add_book(self):
        # 시간 복잡도: O(n)       
        try:
            book_id = input("책 번호를 입력하세요: ")
            title = input("책 제목을 입력하세요: ")
            author = input("저자를 입력하세요: ")
            year = input("출판 연도를 입력하세요: ")
            
            # 책 번호 중복 검사
            if self.book_list.find_by_id(book_id) is not None: # O(n)
                print(f"오류: 이미 존재하는 책 번호입니다. ({book_id})")
                return

            # 새 Book 객체 생성 및 리스트의 맨 뒤에 추가
            new_book = Book(book_id, title, author, year)
            current_size = self.book_list.size() # O(n)
            self.book_list.insert(current_size, new_book) # O(n)
            print(f"도서 '{title}'가 추가되었습니다.")

        except Exception as e:
            print(f"오류 발생: {e}")

    # 2. 도서 삭제 기능 (책 제목 기준)
    def remove_book(self):
        # 시간 복잡도: O(n)
        title = input("삭제할 책 제목을 입력하세요: ")
        pos = self.book_list.find_pos_by_title(title) # O(n)
        
        if pos == -1:
            print(f"오류: '{title}' 도서를 찾을 수 없습니다.")
        else:
            self.book_list.delete(pos) # O(n)
            print(f"책 제목 '{title}'의 도서가 삭제되었습니다.")

    # 3. 도서 조회 기능 (책 제목 기준)    
    def search_book(self):
        # 시간 복잡도: O(n)
        title = input("조회할 책 제목을 입력하세요: ")
        book = self.book_list.find_by_title(title) # O(n)

        if book is None:
            print(f"오류: '{title}' 도서를 찾을 수 없습니다.")
        else:
            print(book)
   
    # 4. 전체 도서 목록 출력 기능
    def display_books(self):
        # 시간 복잡도: O(n)
        print("현재 등록된 도서 목록:")
        if self.book_list.isEmpty(): # O(1)
            print("현재 등록된 도서가 없습니다.")
        else:
            self.book_list.display() # O(n)

    # 5. 프로그램 실행 (메인 루프)     
    def run(self):
        # 시간 복잡도: O(k*n) (k는 사용자가 메뉴를 선택하는 횟수)
        while True:
            print("\n=== 도서 관리 프로그램 ===")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 종료")
            
            choice = input("메뉴를 선택하세요: ")

            if choice == '1':
                self.add_book()      # O(n)
            elif choice == '2':
                self.remove_book()   # O(n)
            elif choice == '3':
                self.search_book()   # O(n)
            elif choice == '4':
                self.display_books() # O(n)
            elif choice == '5':
                print("\n프로그램을 종료합니다.")
                break                 # O(1)
            else:
                print("잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.") # O(1)


# =========================================================
# 도서 관리 프로그램 실행
# =========================================================
if __name__ == "__main__":
    # 시간 복잡도: O(1) (객체 생성)
    app = BookManagement()
    
    # 시간 복잡도: O(k*n) (프로그램 실행, k는 사용자 연산 횟수)
    app.run()