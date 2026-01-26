from testExam.service import *
from testExam.common import Session


def main():
    MemberService.load_members()


    run = True
    while run:
        print("""
    ==============================   
      MBC 아카데미 회원관리 프로그램
    ==============================    
     1. 회원가입      2. 로그인
     3. 로그아웃      4. 마이페이지
     5. 관리자페이지  6. 회원상태 변경
     0. 프로그램 종료
        """)

        member = Session.login_member

        if member is None:
            print("<현재 비로그인 상태>")
            print("로그인 후 이용가능한 사이트입니다.")
            print("계정이 없으시다면 1번을 입력하여 회원가입을 진행해주세요.")

        else:
            print(f"{member.role}, {member.name}님 로그인 성공!")

        sel = input("이용하실 번호를 입력해주세요.\n>>> ")

        if sel == "1":
            MemberService.signup()
        elif sel == "2":
            MemberService.login()
        elif sel == "3":
            MemberService.logout()
        elif sel == "4":
            MemberService.modify()
        elif sel == "5":
            if Session.is_admin() :
                MemberService.admin_menu()
            elif Session.is_manager():
                MemberService.manager_menu()
        elif sel == "6":
            MemberService.delete()
        elif sel == "0":
            print("프로그램을 종료합니다.")
            run = False

if __name__ == "__main__":
    main()