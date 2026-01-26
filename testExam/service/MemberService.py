# 회원가입, 로그인, 로그아웃, 내정보수정(암호,전화번호,이름변경), 관리자페이지(암호,등급,블랙리스트여부), 프로그램종료

import os

from testExam.domain import *
from testExam.common import Session

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..", "data", "member.txt")

class MemberService:

    members = []

    @classmethod
    def load_members(cls):
        cls.members = []

        if not os.path.exists(FILE_PATH):
            cls.save_members()
            return

        with open(FILE_PATH, "r", encoding = "utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))


    @classmethod
    def save_members(cls):
        with open(FILE_PATH, "w", encoding = "utf-8") as f:
            for m in cls.members:
                f.write(m.to_line() + "\n")

    # 회원가입
    @classmethod
    def signup(cls):
        print("\n[회원가입]")
        uid = input("아이디 : ")

        for m in cls.members:
            if m.uid == uid:
                print("이미 존재하는 아이디입니다.")
                print("다른 아이디를 이용해주세요.")
                return

        pw = input("비밀번호 : ")
        name = input("이름 : ")
        number = input("전화번호 : ")

        for m in cls.members:
            if m.number == number:
                print("이미 가입한 이력이 있는 번호입니다.")
                print("다른 번호로 가입해주세요.")
                return

        print("입력한 정보를 확인해주세요.")
        print(f"아이디 : {uid} | 이름 : {name} | 전화번호 : {number}")

        if len(number) == 11 :
            print("전화번호 11자리 입력 확인 완료")

        else:
            print("전화번호 11자리 입력이 확인되지 않았습니다.")
            print("처음부터 다시 시도해주세요.")
            return
        # if len(number[3]) == "-" and len(number[8]) == "-":
        #     print("구문자 입력 확인 완료.")
        #    return
        # else:
        #     print("구문자(-) 입력이 확인되지 않았습니다.")

        # role = "user" (기본값이 user이기 때문에 생략함)

        if input("입력한 정보가 맞으시다면 y를 입력해주세요. >>> ") == "y":
            member = Member(uid, pw, name, number)
            cls.members.append(member)
            cls.save_members()
            print("회원가입이 완료되었습니다.")
        else:
            print("회원가입을 취소하였습니다.")


    # 로그인
    @classmethod
    def login(cls):
        print("\n[로그인]")

        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        for m in cls.members:
            if m.uid == uid:
                if not m.active:
                    print("비활성화된 계정입니다.")
                    print("관리자에게 문의해주세요.")
                    return

                if m.pw == pw:
                    Session.login(m)
                    print(f"{m.role}, {m.name}님 환영합니다.")
                    # print(m)
                    return
                else:
                    print("비밀번호가 틀렸습니다.")
                    print("다시 시도해주세요.")

        print("존재하지 않는 아이디입니다.")

    # 로그아웃
    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요.")
            return

        Session.logout()
        print("로그아웃 완료")

    # 내정보 수정
    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요.")
            return

        member = Session.login_member

        print("""
    ========================
      MBC 아카데미 마이페이지
    ========================
    1. 이름 변경
    2. 비밀번호 변경
    3. 전화번호 변경
    0. 뒤로가기      
            
        """)

        sel = input("수정을 원하시는 번호를 입력해주세요.\n >>> ")

        if sel == "1":
            member.name = input("변경할 이름 : ")
            print("이름 변경이 완료되었습니다.")
        elif sel == "2":
            member.pw = input("변경할 비밀번호 : ")
            print("비밀번호 변경이 완료되었습니다.")
        elif sel == "3":
            member.number = input("변경할 전화번호 : ")
            print("전화번호 변경이 완료되었습니다.")
        else:
            return

        cls.save_members()


    #회원 탈퇴 및 비활성화
    @classmethod
    def delete(cls):
        if not Session.is_login():
            print("로그인 후 이용해주세요.")
            return

        member = Session.login_member

        print("""
    =============================
    MBC 아카데미 계정 상태 변경 페이지    
    =============================
    1. 회원 탈퇴  2. 계정 비활성화
    0. 뒤로가기    
        
        """)

        sel = input("설정하실 번호를 입력해주세요.\n >>> ")

        if sel == "1":
            print("회원 탈퇴 후 계정 복구가 어렵습니다.")
            if input("정말 회원탈퇴를 원하시다면 y를 입력해주세요. \n >>> ") == "y":
                cls.members.remove(member)
                Session.logout()
                cls.save_members()
                print("회원탈퇴가 완료되었습니다.")
            else:
                print("회원탈퇴가 취소되었습니다.")

        elif sel == "2":
            if input("계정 비활성화를 원하시다면 y를 입력해주세요. \n >>> ") == "y":
                member.active = False
                Session.logout()
                cls.save_members()
                print("계정이 비활성화 되었습니다.")
                print("MBC 아카데미 홈페이지 재로그인시 관리자에게 문의해주세요.")
            else:
                print("계정 비활성화가 취소되었습니다.")

        else:
            return

    #관리자 페이지
    @classmethod
    def admin_menu(cls):

        if not Session.is_login() or not Session.login_member.is_admin():
            print("관리자만 이용 가능합니다.")
            return

        while True:
            # 관리자페이지 - 관리자는 전부 변경 가능, 매니저는 1,2,4,5,0번만 가능
            print("""
         =============================
            MBC 아카데미 관리자 페이지   
         =============================
          1. 전체 회원 조회
          2. 비밀번호 변경(임시 번호 발급)
          3. 권한 변경
          4. 블랙리스트 등록
          5. 블랙리스트 해제
          0. 뒤로가기       
            """)

            sel = input("이용하실 번호를 입력해주세요. \n >>> ")

            if sel == "1":
                cls.list_member()

            elif sel == "2":
                print("\n[비밀번호 변경(임시 비밀번호 발급)]")

                uid = input("대상 아이디 : ")
                for m in cls.members:
                    if m.uid == uid:
                        m.pw = input("임시 비밀번호 : ")
                        print("임시 비밀번호가 발급되었습니다.")
                        print("해당 회원에게 임시 비밀번호를 안내해주세요.")
                    # else:
                    #     print("찾으시는 회원정보가 존재하지 않습니다.")
                cls.save_members()

            elif sel == "3":
                cls.change_role()

            elif sel == "4":
                cls.lockrole()

            elif sel == "5":
                cls.unlockrole()

            elif sel == "0":
                break

    # 매니저 메뉴
    @classmethod
    def manager_menu(cls):
        if not Session.is_login() or not Session.login_member.is_manager():
            print("관리자만 이용 가능합니다.")
            return

        while True:
            # 관리자페이지 - 관리자는 전부 변경 가능, 매니저는 1,2,4,5,0번만 가능
            print("""
         =============================
            MBC 아카데미 관리자 페이지   
         =============================
          1. 전체 회원 조회
          2. 비밀번호 변경(임시 번호 발급)
          3. 블랙리스트 등록
          4. 블랙리스트 해제
          0. 뒤로가기       
            """)

            sel = input("이용하실 번호를 입력해주세요. \n >>> ")

            if sel == "1":
                cls.list_member()

            elif sel == "2":
                print("\n[비밀번호 변경(임시 비밀번호 발급)]")

                uid = input("대상 아이디 : ")
                for m in cls.members:
                    if m.uid == uid:
                        m.pw = input("임시 비밀번호 : ")
                        print("임시 비밀번호가 발급되었습니다.")
                        print("해당 회원에게 임시 비밀번호를 안내해주세요.")
                    # else:
                    #     print("찾으시는 회원정보가 존재하지 않습니다.")
                cls.save_members()

            elif sel == "3":
                cls.lockrole()

            elif sel == "4":
                cls.unlockrole()

            elif sel == "0":
                break

    # 전체 회원 조회
    @classmethod
    def list_member(cls):
        print("\n[전체 회원 조회]")
        for m in cls.members:
            print(m)

    # 권한변경
    @classmethod
    def change_role(cls):
        print("\n[권한 변경]")

        uid = input("대상 아이디 : ")
        for m in cls.members:
            if m.uid == uid:

                print("1. 관리자")
                print("2. 매니저")
                print("3. 일반회원")

                sel = input("권한 변경을 원하시는 번호를 입력해주세요. \n >>> ")

                if sel == "1":
                    m.role = "admin"
                    print("관리자로 권한이 변경되었습니다.")
                elif sel == "2":
                    m.role = "manager"
                    print("매니저로 권한이 변경되었습니다.")
                elif sel == "3":
                    m.role = "user"
                    print("일반회원으로 권한이 변경되었습니다.")
                else:
                    print("잘못된 번호를 입력하셨습니다.")

                cls.save_members()
                return
        print("찾으시는 회원정보가 존재하지 않습니다.")

    # 블랙리스트 등록
    @classmethod
    def lockrole(cls):
        print("\n[블랙리스트 등록]")
        uid = input("대상 아이디 : ")
        for m in cls.members:
            if m.uid == uid:
                if input("블랙리스트로 등록을 원하시면 y를 입력해주세요. \n>>> ") == "y":
                    m.active = False
                    m.role = "blacklist"
                    cls.save_members()
                    print("블랙리스트 등록이 완료되었습니다.")
                    return
                else:
                    print("블랙리스트 등록을 취소하였습니다.")
        print("찾으시는 회원정보가 존재하지 않습니다.")


    # 블랙리스트 해제
    @classmethod
    def unlockrole(cls):
        print("\n[블랙리스트 해제]")
        uid = input("대상 아이디 : ")
        for m in cls.members:
            if m.uid == uid:
                if input("블랙리스트 해제를 원하시면 y를 입력해주세요. \n>>> ") == "y":
                    m.active = True
                    m.role = "user"
                    cls.save_members()
                    print("블랙리스트 해제가 완료되었습니다.")
                    return
                else:
                    print("블랙리스트 해제를 취소하였습니다.")
        print("찾으시는 회원정보가 존재하지 않습니다.")