from LMS.service import *
from LMS.common.Session import Session

def main():

    MemberService.load()

    run = True
    while run:
        print("""
=====================================
        MBC 아카데미 관리 시스템        
=====================================
     1. 회원가입     2. 로그인
     3. 로그아웃     4. 회원관리
     5. 게시판      6. 성적관리
     7. 상품몰      8. 관리자
     0. 종료   
        
        """)

        member = Session.login_member
        if member is None:
            print("현재 로그인 상태가 아닙니다.")
        else:
            print(f"{member.name}님 환영합니다.")

        sel = input(">>> ")
        if sel == "1":
            print("회원가입 페이지로 진입합니다.")
            MemberService.signup()
        elif sel == "2":
            print("로그인 페이지로 진입합니다.")
            MemberService.login()
        elif sel == "3":
            print("로그아웃 페이지로 진입합니다.")
            MemberService.logout()
        elif sel == "4":
            print("회원관리 페이지로 진입합니다.")
            MemberService.modify()
        elif sel == "8":
            print("관리자 페이지로 진입합니다.")
            MemberService.admin_menu()
        elif sel == "0":
            print("시스템을 종료합니다.")
            run = False

if __name__ == "__main__":
    main()