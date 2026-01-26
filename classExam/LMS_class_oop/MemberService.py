# Member 객체에 CRUD 기능을 넣는다.
# 메뉴 구현
# 텍스트 파일 처리(파일 읽기, 파일 저장)
# 회원가입, 로그인, 로그아웃, 회원수정, 회원탈퇴

import os
from Member import Member  # 회원 객체 추가 연결

# 사용법
# member = Member()  -> 객체 생성
# member.필드 또는 메서드로 사용가능

class MemberService:
    def __init__(self, file_name = "member.txt"):
        # 클래스가 생성할 때 초기값 관리
        self.file_name = file_name
        self.members = []  # 회원들을 리스트로 만들어 Member() 객체를 담는다.
        self.session = None   # 로그인 상태들을 담당(members의 인덱스 보관용)
        # 나중에 추가 -> 파일에서 불러오는 메서드
        self.load_members()  # 아래쪽 메서드 호출

    def run(self):
        run = True
        while run:
            self.main_menu()
            sel = input(">>> ")

            if sel == "1": self.member_add()
            elif sel == "2": self.member_login()
            elif sel == "3": self.member_logout()
            elif sel == "4": self.member_modify()
            elif sel == "5": self.member_delete()
            elif sel == "9": run = False
            else:
                print("잘못 입력하셨습니다.")

    def load_members(self):
        # 파일에서 메모리로 불러온다.

        if not os.path.exists(self.file_name):
            self.save_members()
            return

        self.members = []  # 메모리에 남은 값을 초기화
        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:
                self.members.append(Member.from_line(line))
                #                   Member객체에 .from_line() 메서드 실행
                #                                  한줄을 가져와 클래스로 만듬
                #     members 리스트 뒷부분에 추가

    def main_menu(self):
        print("""
===== 회원가입 프로그램 (Member 객체 기반) =====
 1. 회원가입   2. 로그인   3. 로그아웃
 4. 회원정보 수정   5. 회원탈퇴   9. 종료      
      
        """)

    # 회원가입
    def member_add(self):
        print("\n[회원가입]")

        uid = input("아이디 : ")

        if self.find_member(uid):  # 자주쓰는 중복코드로 메서드 처리함.
            print("이미 존재하는 아이디입니다.")
            return

        pw = input("비밀번호 : ")
        name = input("이름 : ")
        role = "user"

        if input("회원가입을 하시겠습니까? y : ") == "y":

            self.members.append(Member(uid, pw, name, role))
            #                   member 클래스의 init 메서드로 바로 들어가 객체 생성
            self.save_members()  # 파일로 기록
            self.load_members()  # 파일에서 다시 불러와
            print("회원가입 완료")

    # 로그인
    def member_login(self):
        if self.session is not None:
            print("이미 로그인한 사용자입니다.")
            return

        print("\n[로그인]")

        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        member = self.find_member(uid)

        if not member:
            print("존재하지 않는 아이디입니다.")
            return

        if not member.active:
            print("비활성화 계정입니다.")
            return

        # if member.id == uid:
        #     print("이미 로그인한 사용자입니다.")
        #     return

        if member.pw == pw:
            self.session = member
            print(f"{member.name}님 로그인 성공({member.role})")

            if member.role == "admin":
                self.member_admin()
                # 관리자용 메서드로 들어감
        else:
            print("비밀번호 오류)")

    # 로그아웃
    def member_logout(self):
        if self.session is None:
            print("로그인 후 이용해주세요.")
            self.member_login()
            return

        self.session = None
        print("로그아웃이 완료되었습니다.")

    # 내정보 수정
    def member_modify(self):
        if self.session is None:
            print("로그인 후 이용해주세요.")
            self.member_login()
            return

        print("\n[내 정보 수정]")
        print("1. 비밀번호 변경")
        print("2. 이름 변경")

        sel = input("선택 : ")

        if sel == "1":
            self.session.pw = input("새 비밀번호 : ")
            print("비밀번호 변경이 완료되었습니다.")
        elif sel == "2":
            self.session.name = input("새 이름 : ")
            print("이름 변경이 완료되었습니다.")

        self.save_members()

    # 회원 탈퇴
    def member_delete(self):
        if self.session is None:
            print("로그인 후 이용해주세요.")
            self.member_login()
            return

        print("\n[회원 탈퇴 및 계정 비활성화]")
        print("1. 회원 탈퇴")
        print("2. 계정 비활성화")

        sel = input("선택 : ")

        if sel == "1":
            if input("정말 회원 탈퇴를 진행하시겠습니까? y : ") == "y":
                self.session.remove(self.session)
                self.session.active = None
                print("회원 탈퇴가 완료되었습니다.")
            else:
                print("회원 탈퇴가 취소되었습니다.")

        elif sel == "2":
            if input("계정 비활성화를 진행하시겠습니까? y : ") == "y":
                self.session.active = False
                self.session = None
                print("계정 비활성화가 완료되었습니다.")
                print("다시 계정 사용을 원하실 경우 관리자에게 문의해주세요.")
            else:
                print("계정 비활성화를 취소하였습니다.")

        self.save_members()

    # 파일 저장용 코드
    def save_members(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for member in self.members:
                f.write(member.to_line())
                #       Member 객체의 메서드를 사용하여 한줄씩 기록

    # id를 이용해 members에서 찾는 공통 메서드
    def find_member(self, uid):
        for member in self.members:
        # memers 리스트에서 한개씩 member객체를 가져와
            if member.id == uid:
            # 가져온 member객체와 .id와 전달받은 id가 같은지
                print(member.name, "님을 찾았습니다.")
                # 예전에는 member[2]로 찾았는데 지금은 변수명으로 찾을 수 있음.
                return member
                # 같은게 있으면 member 객체를 리턴
        return None  # 없으면 None으로 리턴

    def member_admin(self):
        # role = "admin"에 진입 가능한 메서드
        subrun = True
        while subrun:
            print("\n[관리자 메뉴]")
            print("1. 회원 리스트 조회")
            print("2. 비밀번호 변경")
            print("3. 블랙리스트 처리")
            print("4. 블랙리스트 해제")
            print("5. 권한 변경")
            print("9. 종료")

            sel = input("선택 : ")

            # 회원 목록 보기
            if sel == "1":
                self.show_member_list()

            # 비밀번호 변경
            elif sel == "2":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.pw = input("새 비밀번호 : ")
                    self.save_members()
                    print("비밀번호 변경 완료")
                else:
                    print("찾으시는 회원이 존재하지 않습니다.")

            # 블랙리스트 등록
            elif sel == "3":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)

                if member:
                    member.role = "blacklist"
                    member.active = False
                    self.save_members()
                    print("블랙리스트 등록 완료")
                else:
                    print("찾으시는 회원이 존재하지 않습니다.")

            # 블랙리스트 해제
            elif sel == "4":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)

                if member:
                    member.role = "user"
                    member.active = True
                    self.save_members()
                    print("블랙리스트 해제 완료")
                else:
                    print("찾으시는 회원이 존재하지 않습니다.")

            # 권한 변경
            elif sel == "5":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    print("1. 관리자")
                    print("2. 매니저")
                    print("3. 일반사용자")
                    role = input("선택 : ")

                    if role =="1":
                        member.role = "admin"
                        print("관리자로 권한이 변경되었습니다.")
                    elif role =="2":
                        member.role = "manager"
                        print("매니저로 권한이 변경되었습니다.")
                    elif role =="3":
                        member.role = "user"
                        print("일반 사용자로 권한이 변경되었습니다.")

                    self.save_members()
                else:
                    print("찾으시는 회원이 존재하지 않습니다.")

            elif sel == "9":
                subrun = False


    def show_member_list(self):
        # 관리자가 볼 수 있는 회원 리스트
        print("\n[회원 목록]")
        print("-"*60)
        print(f"{'ID':10} {'이름':10} {'권한':10} {'상태'}")
        print("-"*60)

        for member in self.members:
        # members 리스트에 있는 객체를 하나씩 가져와 member에 넣음
            status = "활성" if member.active else "비활성"
            # member.active == True면 status변수에 "활성" 이라고 넣고 아니면 "비활성"
            print(f"{member.id:10} {member.name:10} {member.role:10} {status}")
            #                                                     "활성" or "비활성"
        print("-"*60)

