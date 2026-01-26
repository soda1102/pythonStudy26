# 회원 관리용 코드를 만든다.
# c -> 회원추가
# r -> 관리자일경우 (전체회원보기), 일반회원인 경우 (로그인)
# u -> 관리자일경우 (회원차단, 암호변경문의), 일반회원인 경우 (내정보수정, 암호변경)
# d -> 회원탈퇴

# 메뉴구현
run = True # 프로그램 동작중을 관리하는 변수

menu = """
======================================
      mbc 아카데미 회원관리 프로그램
======================================
1. 회원가입
2. 로그인
3. 회원보기
4. 내정보 수정
5. 프로그램 종료
"""

# 사용할 리스트 변수를 생성한다.
sns = [1, 2]   # 사용자 관리번호(학번)
ids = ["kkw", "lhj"]   # 로그인용 아이디
passwords = ["1234", "4321"]   # 로그인용 패스워드
names = ["관리자", "임효정"]   # 사용자명
emails = ["admin@mbc.com", "lhj@mbc.com"]   # 이메일주소
admins = [True,False]   # 관리자 유무 / 관리자면 True , 일반사용자 False


while run:
    print(menu)
    select = input("1~5숫자를 입력하세요 : ")
    if select == "1":
        print("회원가입 메뉴에 진입하였습니다.")
        sn = input("사번을 입력하세요 : ")
        id = input("아이디를 입력하세요 : ")
        pw = input("암호를 입력하세요 : ")
        name = input("이름을 입력하세요 : ")
        email = input("이메일 주소를 입력하세요 : ")
        admin = False

        print("입력된 값을 확인하시고 y를 누르면 가입됩니다.")
        print("이름 : " + name)
        print("id" + id)
        print("pw" + pw)
        print("name" + name)
        print("email" + email)
        if input("y/n") == "y" :
            sns.append(sn)
            ids.append(id)
            passwords.append(pw)
            names.append(name)
            emails.append(email)
            print("입력이 완료되었습니다.")
        else :
            print("처음부터 다시 입력하세요.")

    elif select == "2":
        print("로그인 메뉴에 진입하였습니다.")
        id = input("아이디를 입력하세요 : ")
        pw = input("암호를 입력하세요 : ")

    elif select == "3":
        print("회원정보 보기 메뉴에 진입하였습니다.")

    elif select == "4":
        print("내정보수정 페이지 입니다.")

    elif select == "5":
        print("회원가입 프로그램이 종료됩니다.")
        run = False

    else :
        print("1~5사이 값을 입력하세요!")

