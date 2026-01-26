import os

from packageExam.LMS.domain import *
from packageExam.LMS.common import Session

#회원 데이터 파일 경로

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..", "data", "member.txt")

class MemberService:
    # 회원관련
    members = []

    #파일에 있는 데이터를 한줄씩 읽어 Member객체로 만들어 리스트에 추가
    @classmethod
    def load(cls):
        cls.members = []

        if not os.path.exists(FILE_PATH):
            cls.save()
            return

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))

    #메모리에 있는 members[]를 텍스트 파일로 저장
    @classmethod
    def save(cls):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for m in cls.members:
                f.write(m.to_line() + "\n")

    #로그인
    @classmethod
    def login(cls):
        print("\n[로그인]")

        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        for m in cls.members:
            if m.uid == uid:
                if not m.active:
                    print("비활성화된 계정입니다.")
                    return

                if m.pw == pw:
                    Session.login(m)  #로그인 성공시 Session객체에 member객체를 넣음
                    print(f"{m.role}, {m.name}님 로그인 성공")
                    print(m)
                    return
                else:
                    print("비밀번호가 틀렸습니다.")
                    return
        print("존재하지 않는 아이디입니다.")

    #로그아웃
    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요.")
            return

        Session.logout()
        print("로그아웃 완료")

    #회원가입
    @classmethod
    def signup(cls):
        print("\n[회원가입]")
        uid = input("아이디 : ")

        if any(m.uid == uid for m in cls.members):
            print("이미 존재하는 아이디입니다.")
            return

        pw = input("비밀번호 : ")
        name = input("이름 : ")
        number = input("전화번호 : ")

        print(f"아이디 : {uid}, 이름 : {name}, 전화번호 : {number}")

        if input("입력한 사항을 확인 후 저장을 원하시면 y를 입력해주세요 : ") == "y":
            member = Member(uid, name, pw, number)
            cls.members.append(member)
            cls.save()
            print("저장이 완료되었습니다.")

        else:
            print("회원가입을 취소하였습니다.")

    #내정보수정
    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요.")
            return

        member = Session.login_member

        print("""
    [내 정보 수정]
    1. 이름 변경
    2. 비밀번호 변경
    3. 전화번호 변경
    0. 뒤로가기
               
        """)

        sel = input("정보 수정을 원하시는 번호를 입력해주세요 : ")

        if sel == "1":
            member.name = input("새 이름 : ")
            print("이름 변경이 완료되었습니다.")

        elif sel == "2":
            member.pw = input("새 비밀번호 : ")
            print("비밀번호 변경이 완료되었습니다.")

        elif sel == "3":
            member.number = input("새 전화번호 : ")
            print("전화번호 변경이 완료되었습니다.")

        else:
            return

        cls.save()

    #회원 탍퇴 및 비활성화
    @classmethod
    def delete(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요.")
            return

        member = Session.login_member

        print("""
        [회원 탈퇴 및 비활성화]
        1. 회원 탈퇴
        2. 비활성화(휴먼계정)
        0. 뒤로가기
                """)

        sel = input("원하시는 번호를 입력해주세요 : ")

        if sel == "1":
            if input("회원 탈퇴 후 취소가 어렵습니다.\n정말 회원 탈퇴를 원하시면 y를 입력해주세요 : ") == "y":
                cls.members.remove(member)
                Session.logout()
                cls.save()
                print("회원탈퇴가 완료되었습니다.")
            else:
                print("회원탈퇴가 취소되었습니다.")

        elif sel == "2":
            if input("계정 비활성화를 진행하시겠습니까? y : ") == "y":
                member.active = False
                Session.logout()
                cls.save()
                print("계정이 비활성화 되었습니다.\n재로그인 시 관리자에게 문의하여 주세요.")
            else:
                print("계정 비활성화가 취소되었습니다.")

        else:
            return

    #관리자메뉴
    @classmethod
    def admin_menu(cls):
        if not Session.is_login() or not Session.login_member.is_admin():
            print("관리자만 이용 가능한 메뉴입니다.")
            return

        while True:
            print("""
        [관리자 메뉴]    
        1. 회원 목록 조회
        2. 권한 변경
        3. 블랙리스트 등록
        4. 블랙리스트 해제
        0. 뒤로가기    
            """)

            sel = input("원하시는 번호를 입력해주세요 : ")

            if sel == "1":
                cls.list_members()
            elif sel == "2":
                cls.change_role()
            elif sel == "3":
                cls.blockrole()
            elif sel == "4":
                cls.unblockrole()
            elif sel == "0":
                break

    #멤버목록
    @classmethod
    def list_members(cls):
        print("\n[회원 목록]")
        for m in cls.members:
            print(m)

    #권한변경
    @classmethod
    def change_role(cls):
        print("권한 변경")
        uid = input("대상 아이디 : ")
        for m in cls.members:
            if m.uid == uid:

                print("1. 관리자")
                print("2. 매니저")
                print("3. 일반회원")

                sel = input("변경할 권한 입력 : ")

                if sel == "1":
                    m.role = "admin"
                    print("권한이 관리자로 변경되었습니다.")
                elif sel == "2":
                    m.role = "manager"
                    print("권한이 매니저로 변경되었습니다.")
                elif sel == "3":
                    m.role = "user"
                    print("권한이 일반회원으로 변경되었습니다.")
                else:
                    print("잘못된 번호를 입력하셨습니다.")

                cls.save()
                return

        print("찾으시는 회원이 존재하지 않습니다.")

    #블랙리스트등록
    @classmethod
    def blockrole(cls):
        print("블랙리스트 등록")
        uid = input("대상 아이디 : ")
        for m in cls.members:
            if m.uid == uid:
                m.active = False
                m.role = "blacklist"
                cls.save()
                print("블랙리스트 등록이 완료되었습니다.")
                return
        print("찾으시는 회원이 존재하지 않습니다.")

    #블랙리스트해제
    @classmethod
    def unblockrole(cls):
        print("블랙리스트 해제")
        uid = input("대상 아이디 : ")
        for m in cls.members:
            if m.uid == uid:
                m.active = True
                m.role = "user"
                cls.save()
                print("블랙리스트 해제가 완료되었습니다.")
                return
        print("찾으시는 회원이 존재하지 않습니다.")