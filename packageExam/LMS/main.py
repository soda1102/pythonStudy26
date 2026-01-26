from packageExam.LMS.service import *
from packageExam.LMS.common import Session

def main():
    MemberService.load()

    run = True
    while run:
        print("""
    ========================================
     MBC 아카데미 홈페이지에 오신 것을 환영합니다.    
    ========================================    
    1. 회원가입      2. 로그인      3. 로그아웃  
    4. 회원관리(관리자)   5. 게시판   6. 성적관리
    7. 상품몰   0. 홈페이지 종료
        
        """)

        member = Session.login_member

        if member is None:
            print("로그인 후 이용해주세요.(현재 로그아웃 상태)")
        else:
            print(f"{member.name}님 로그인 성공!")

        sel = input("원하는 번호를 입력해주세요 : ")

        if sel == "1":
            MemberService.signup()
        elif sel == "2":
            MemberService.login()
        elif sel == "3":
            MemberService.logout()
        elif sel == "4":
            MemberService.admin_menu()
        elif sel == "5":
            BoardService.run()
        elif sel == "6":
            ScoreService.run()
        elif sel == "7":
            ItemService.run()
        elif sel == "0":
            print("프로그램을 종료합니다.")
            run = False


if __name__ == "__main__":
    main()