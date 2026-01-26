import os

from packageExam.LMS.domain import Board
from packageExam.LMS.common import Session

FILE_PATH = "data/board.txt"

class BoardService:
    boards = []

    @classmethod
    def load(cls):
        if not os.path.exists(FILE_PATH):
            return
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            cls.boards = [Board.from_line(line) for line in f]

    @classmethod
    def save(cls):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for b in cls.boards:
                f.write(b.to_line() + "\n")

    #게시글 등록
    @classmethod
    def write(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요.")
            return

        title = input("제목 : ")
        content = input("내용 : ")
        writer = Session.login_member.uid

        if input("작성을 완료하셨다면 y를 입력하여 저장해주세요 : ") == "y":
            no = len(cls.boards) + 1
            cls.boards.append(Board(no, title, content, writer))
            cls.save()
            print("게시글 등록이 완료되었습니다.")

    #게시글 목록
    @classmethod
    def list(cls):
        print("\n[게시글 목록]")
        print(f"No. 제목 | 내용 | 작성자")
        for b in cls.boards:
            if b.active:
                print(f"{b.no} | {b.title} | {b.content} | {b.writer}")

    #게시글 삭제
    @classmethod
    def delete(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요.")
            return

        no = int(input("삭제할 게시글 번호 : "))

        for b in cls.boards:
            if b.no == no:
                if Session.login_member.uid == b.writer or Session.login_member.role == "admin":
                    if input("게시글 삭제 후 복구가 불가능합니다. 삭제하시려면 y를 입력해주세요 : ") == "y":
                        b.active = False
                        cls.save()
                        print("게시글 삭제가 완료되었습니다.")
                    else:
                        print("게시글 삭제가 취소되었습니다.")
                else:
                    print("권한이 없습니다.")
                return

    #게시글 자세히보기
    @classmethod
    def moreread(cls):

        no =  int(input("확인할 게시글 번호 : "))

        for b in cls.boards:
            if b.no == no:
                b.visitcount += 1

                print("-"*50)
                print(f"제목 : {b.title}")
                print(f"내용 : {b.content}")
                print(f"작성자 : {b.writer}")
                print(f"조회수 : {b.visitcount}")
                print(f"좋아요 : {b.hit}")
                print("-" * 50)

                if input("공감을 누르시겠습니까? y : ") == "y":
                    b.hit += 1
                    print("좋아요 + 1")
                else:
                    print("공감 하지 않으셨습니다.")

                cls.save()
                return

        print("찾으시는 게시글 번호가 존재하지 않습니다.")

    #게시글 수정하기
    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요.")
            return

        no = int(input("수정할 게시글 번호 : "))

        for b in cls.boards:
            if b.no == no:
                if Session.login_member.uid == b.writer or Session.login_member.role == "admin":
                    print(f"제목 : {b.title}, 내용 : {b.content}, 작성자 : {b.writer}")
                    print("위 게시글의 수정할 항목을 선택해주세요.")
                    print("1. 제목")
                    print("2. 내용")
                    print("3. 뒤로가기")

                    sel = input(">>> ")

                    if sel == "1":
                        b.title = input("새 제목 : ")
                        print("제목이 수정되었습니다.")
                    elif sel == "2":
                        b.content = input("새 내용 : ")
                        print("내용이 수정되었습니다.")
                    elif sel == "3":
                        return

                    cls.save()
        print("찾으시는 게시글이 존재하지 않습니다.")

    #시작
    @classmethod
    def run(cls):
        cls.load()

        while True:
            print("""
        [게시판 메뉴]
        1. 게시글 작성하기
        2. 게시글 목록 확인하기
        3. 게시글 삭제하기
        4. 게시글 자세히보기
        5. 게시글 수정하기
        0. 뒤로가기
            
            """)

            sel = input("원하는 번호를 입력해주세요 : ")

            if sel == "1":
                cls.write()
            elif sel == "2":
                cls.list()
            elif sel == "3":
                cls.delete()
            elif sel == "4":
                cls.moreread()
            elif sel == "5":
                cls.modify()
            elif sel == "0":
                break