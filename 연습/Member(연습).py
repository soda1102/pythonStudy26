# 회원 관리용 코드를 만든다.
# c -> 회원추가
# r -> 관리자일경우 (전체회원보기), 일반회원인 경우 (로그인)
# u -> 관리자일경우 (회원차단, 암호변경문의), 일반회원인 경우 (내정보수정, 암호변경)
# d -> 회원탈퇴

# 메뉴구현
run = True # 프로그램 동작중을 관리하는 변수
login_user = None  # 현재 로그인한 사용자 인덱스

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
        sn = int(input("사번을 입력하세요 : "))
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

        id = input("아이디 : ")
        pw = input("비밀번호 : ")

        if id in ids:
            idx = ids.index(id)
            if passwords[idx] == pw :
                login_user = idx
                print(f"{names[idx]}님 로그인 성공")

                if admins[idx] :
                    print("> 관리자 계정입니다.")
                else:
                    print("> 일반회원 계정입니다.")
            else :
                print("비밀번호가 틀렸습니다.")
        else :
            print("회원정보가 존재하지 않습니다.")

    elif select == "3":
        if login_user is None :
            print("로그인 후 이용 가능합니다.")
            continue

        if admins[login_user] : #관리자
            print("\n[전체 회원 목록]")
            for i in range(len(ids)) :
                print(f"{i+1}. {names[i]} ㅣ {ids[i]} ㅣ {emails[i]} ㅣ 관리자:{admins[i]}")
        else : #일반회원
            print("\n[내 정보]")
            print(f"이름 : {names[login_user]}")
            print(f"아이디 : {ids[login_user]}")
            print(f'이메일 : {emails[login_user]}')
            print(f'사번 : {sns[login_user]}')

    elif select == "4":
        if login_user is None :
            print("로그인 후 이용 가능합니다.")
        else :
            print("내 정보수정 페이지 입니다.")
            continue

        newPw = input("새암호입력")
        pws[login_user] = newPw
        newName = input("새이름입력")
        names[login_user] = newName
        newM = input("새이메일입력")
        email[login_user] = newM

    elif select == "5":
        print("회원가입 프로그램이 종료됩니다.")
        run = False

    else :
        print("1~5사이 값을 입력하세요!")

