# 회원관리 CRUD를 사용자 지정 함수로 만들어보자
# C : 회원가입
# R : 회원 리스트 관리자인 경우 회원 암호 변경, 블랙리스트 생성, 권한부여
# R : 로그인 id와 pw를 활용하여 로그인 상태 유지 session
# U : 회원 정보 수정
# D : 회원 탈퇴, 회원 비활성화

# 프로그램에서 사용될 변수들
# 전역변수(global) -> py 파일 안에서 전체적으로 사용되는 변수
# 지역변수(local) -> while, if for, def 안에서 사용되는 변수
run = True # while에서 전체적으로 사용되는 변수(프로그램 구동)
session = None # 로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용

# 프로그램에서 사용될 리스트들(더미 데이터)
# sns = [1,2,3]  #회원번호(미사용 사유 : 회원 삭제 및 추가시 번호가 흔들림, index로만 사용)
ids = ["kkw","lhj","ljj"]  #로그인 id들
pws = ["1234","5678","8888"]  #암호들
names = ["김기원","임효정","이재정"]  #사용자명
roles = ["admin","manager","user"]  #사용자권한(admin, manager, user)
active = [True,True,True]  #회원사용중, 탈퇴, 휴먼, 블랙리스트 여부 등
# 차후에는 파일처리로 변환할 예정

# 프로그램에서 사용될 함수들

# ===== C : 회원가입 =====
def member_add():
    # 회원가입용 함수
    print("member_add 함수로 진입합니다.") # 나중에 주석처리하기
    # 회원가입에 필요한 기능을 넣기
    new_id = input("아이디 : ")   # 키보드로 아이디를 넣음

    # 이미 아이디가 존재하면 다른 아이디로 넣게 유도
    if new_id in ids:   # ids에서 id를 찾아 있는지 확인
        # True일때
        print("이미 존재하는 아이디입니다.")
        return   # if문 종료

    else:   # False일때 ids에 입력된 id가 없을때(중복X)
        new_pw = input("비밀번호 : ")
        new_name = input("이름 : ")
        member_add_menu()   # 회원권한 메뉴 출력

        role_set = input("권한 선택 : ")
        if role_set == "1":
            new_role = "admin"
        elif role_set == "2":
            new_role = "manager"
        else:
            new_role = "user"

        print(f"""
입력된 정보를 확인하세요!
이름 : {new_name} | 아이디 : {new_id} | 암호 : {new_pw} | 권한 : {new_role}""")

        # print("저장하려면 y : ")

        save_select = input("저장하려면 y : ")
        if save_select == "y":
            print("저장을 시작합니다.")

            ids.append(new_id)
            pws.append(new_pw)
            names.append(new_name)
            roles.append(new_role)
            active.append(True)   # 저장완료

            print("저장이 완료되었습니다.")

            # 차후에 로그인 함수 추가해보기
        else:
            print("회원가입이 완료되지 않았습니다.")

    print("member_add 함수를 종료합니다.")
# 회원가입용 함수 종료

# ===== R : 로그인상태 유지 =====
def member_login():
    # 가입된 회원을 확인하여 로그인 처리 후 session변수에 인덱스를 넣음
    print("member_login 함수로 진입합니다.") # 나중에 주석처리하기
    # 회원가입에 필요한 기능을 넣기

    global session   # 맨 뒤에 전역변수로 지정한 내용 활용

    if session is not None:   # session에 이미 값이 있으면?
    # is not None 싱글톤이라는 객체가 있는지 비교하는 용도
    # if session != None -> 숫자 비교형 이퀄이나 는 값으로 사용
        # True
        print("이미 로그인한 상태입니다.")
        print(f"로그인한 사용자는 {names[session]}님 입니다.")
        return   # 되돌아감
    else:
        # False
        user_id = input("로그인 ID : ")
        user_pw = input("로그인 PW : ")

        if user_id in ids :   #키보드로 받은 id가 ids에 있는지?
            # True
            idx = ids.index(user_id)   # id에 해당하는 주소를 idx에 넣음
            if not active[idx]:   # 회원 활성화 상태인지?
                # False (not이 있기 때문에)
                print("비활성화 / 차단된 계정입니다.")
                return
            else:
                # True
                # 암호를 비교한다.
                if user_pw == pws[idx]:  # 키보드로 넣은 암호와 리스트의 주소 암호가 일치하는지 확인
                    # id도 같고 활성화 상태이고 암호가 같다
                    session = idx  # 로그인 상태로 완성
                    # 글로벌 영역에 session 값(로그인한 사용자의 주소)이 있는 상태가 됨

                    print(f"{names[session]}님 환영합니다.")
                    print(f"{roles[idx]}권한을 가지고 있습니다.")
                else:
                    print("비밀번호가 틀렸습니다.")
        else:
            # False
            print("존재하지 않는 아이디입니다.")


    print("member_login 함수를 종료합니다.")
# 회원 로그인용 함수 종료

# ===== R : 관리자인 경우 회원 암호 변경, 블랙리스트, 권한 변경 =====
def member_admin():
    # 관리자가 로그인 했을 경우 할 수 있는 기능을 작성
    print("member_admin 함수로 진입합니다.")
    # 다른 사용자 암호 변경 코드

    # 블랙리스트 변한 -> active(False처리)

    # 권한부여 -> 사용자의 권한 roles를 변경(manager, user)

    print("member_admin 함수를 종료합니다.")
    # 관리자가 사용자 변경사항 함수 종료

# ===== R : 로그아웃 =====
def member_logout():
    # 회원 로그아웃으로 상태 변경 -> session값을 None으로 변경
    print("member_logout 함수로 진입합니다.")
    # 사용자가 로그인 상태인지 확인하고 session을 None로 변경

    print("member_logout 함수를 종료합니다.")
    # 로그아웃 함수 종료

# ===== U : 회원 정보 수정 =====
def member_modify():
    # 가입된 회원의 정보를 수정
    print("member_modify 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 자신의 정보를 확인하고 수정

    print("member_modify 함수를 종료합니다.")
    # 회원 정보 수정사항 함수 종료

# ===== D : 회원탈퇴, 비활성화 =====
def member_delete():
    # 회원 탈퇴 또는 회원 휴먼등 처리
    print("member_delete 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 탈퇴는 pop, 휴먼(active=False처리)

    print("member_delete 함수를 종료합니다.")
    # 회원 탈퇴 및 비활성화 함수 종료

# --------------------------기능에 대한 함수 생성 끝--------------------------

# ===== 사용할 메인 메뉴 =====
def main_menu():
    print(f"""
================================
MBC 아카데미 회원관리 프로그램입니다.    
================================   

1. 회원가입
2. 로그인
3. 로그아웃
4. 회원 정보 수정
5. 회원 탈퇴

9. 프로그램 종료
    """)
    # 메인 메뉴용 함수 종료

# ===== 사용할 회원가입 메뉴 =====
def member_add_menu():
    print(f"""
-----------------------------------
  MBC 아카데미 회원 권한을 확인하세요.    
-----------------------------------
 1. 관리자  2. 매니저  3. 일반 사용자
    """)
    # 회원가입 메뉴 함수 종료

# ===== 사용할 로그인 메뉴 =====


# --------------------------메뉴 함수 생성 끝--------------------------

# 프로그램 시작
while run:   # 메인 프로그램 실행 코드
    main_menu()   #위에서 만든 메인메뉴 실행 (ctrl+클릭하면 해당 메뉴로 이동)

    select = input(">>>")   # 키보드로 메뉴 선택

    if select == "1":   # 회원가입코드
        member_add()   # 회원 가입용 함수 호출

    elif select == "2":   # 로그인
        member_login()   # 로그인용 함수 호출

    elif select == "3":   # 로그아웃
        member_logout()   # 로그아웃 함수 호출

    elif select == "4":   # 회원정보수정
        member_modify()   # 회원 정보 수정 함수 호출

    elif select == "5":   # 회원탈퇴, 비활성화
        member_delete()   # 회원 탈퇴 함수 호출

    elif select == "9":   # 프로그램 종료
        run = False

    else:
        print("잘못 입력 하셨습니다.")

    # while문 종료

