# c : 회원가입
# r : 관리자 - 암호변경, 권한부여, 블랙리스트 생성 ,, 일반 - 로그인 ,,  로그아웃
# u : 정보수정
# d : 회원탈퇴 및 비활성화


run = True
session = None  #로그인사용자

# 회원가입 변수
ids = ["ksh"]  #아이디
pws = ["1234"]  #비번
names = ["김소현"]  #이름
numbers = ["01012345678"]  #전화번호
groups = ["admin"]  #권한 (admin, manager, user)
active = [True]  #회원권한여부

# == 회원가입 ==
def member_add():  #회원가입
    print("회원가입 메뉴에 진입하셨습니다.")

    new_id = input("아이디 : ")

    if new_id in ids:
        print("이미 존재하는 아이디입니다.")
        return
    else:
        new_pw = input("비밀번호 : ")
        new_name = input("이름 : ")
        new_number = input("전화번호 : ")

        if new_number in numbers:
            print("이미 등록되어있는 전화번호입니다.")
            print("등록된 정보가 있는지 확인해주세요.")
            return

        print("\n입력된 정보를 확인해주세요.")
        print(f"아이디 : {new_id} | 이름 : {new_name} | 전화번호 : {new_number}")

        save_select = input("\n가입하시려면 y : ")
        if save_select == "y":
            ids.append(new_id)
            pws.append(new_pw)
            names.append(new_name)
            numbers.append(new_number)
            groups.append("user")
            active.append(True)
            print("가입이 완료되었습니다.")
        else:
            print("회원가입이 완료되지 않았습니다.")


def member_admin():   #관리자용

    global session

    if session is None:
        print("관리자만 이용할 수 있습니다.")
        return

    else:
        if groups[session] == "admin":   #매니저도 수정가능하게 하려면 or groups[session] == "manager"로 추가해줄것.
            member_add_menu()

            menu_select = input("원하시는 번호를 입력해주세요 >>> ")

            if menu_select == "1":
                print("\n[전체 회원 정보 보기]")
                print("-"*50)
                print("순번 | 이름 | 아이디 | 비밀번호 | 전화번호 | 회원권한")
                print("-"*50)

                for i in range(len(names)):
                    print(f"순번 : {i} | 이름 : {names[i]} | 아이디 : {ids[i]} | 비밀번호 : {pws[i]} | 전화번호 : {numbers[i]} | 회원권한 : {groups[i]}")

            elif menu_select == "2":
                print("\n[권한 설정]")

                gp_id = input("권한을 변경하실 아이디를 입력해주세요 >>> ")   # 그룹 변경할 사람 이름

                if gp_id in ids:
                    idx = ids.index(gp_id)

                    print(f"\n현재 권한은 {groups[idx]} 입니다.")
                    member_group_menu()
                    role = input(">>> ")

                    if role == "1":
                        print("권한이 관리자로 변경되었습니다.")
                        groups[idx] = "admin"

                    elif role == "2":
                        print("권한이 매니저로 변경되었습니다.")
                        groups[idx] = "manager"

                    elif role == "3":
                        print("권한이 일반회원으로 변경되었습니다.")
                        groups[idx] = "user"

                    else:
                        print("잘못 입력되었습니다.")

                else:
                    print("찾으시는 아이디가 존재하지 않습니다.")

            elif menu_select == "3":
                print("\n[블랙리스트 등록]")

                u_id = input("\n블랙리스트 설정할 회원 아이디 : ")
                if u_id in ids:
                    idx = ids.index(u_id)
                    active[idx] = False
                    print(f"{names[idx]}님이 블랙리스트에 등록되었습니다.")
                    groups[idx] = "blacklist"
                else:
                    print("찾으시는 아이디가 존재하지 않습니다.")

            elif menu_select == "4":
                print("\n[회원 비밀번호 변경]")

                u_id = input("비밀번호 변경할 회원 아이디 : ")
                if u_id in ids:
                    idx = ids.index(u_id)
                    pws[idx] = input("새 비밀번호 : ")
                    print("비밀번호 변경이 완료되었습니다.")
                else:
                    print("찾으시는 회원 아이디가 존재하지 않습니다.")

            elif menu_select == "5":
                print("\n[블랙리스트 해제]")

                b_id = input("\n블랙리스트 해제할 회원 아이디 : ")
                if b_id in ids:
                    idx = ids.index(b_id)
                    active[idx] = True
                    print(f"{names[idx]}님이 블랙리스트에서 해제되었습니다.")
                    groups[idx] = "user"
                else:
                    print("찾으시는 아이디가 존재하지 않습니다.")

            elif menu_select == "6":
                print("메인메뉴로 돌아갑니다.")

            else:
                print("잘못 입력하셨습니다.")
        else:
            print("관리자로 로그인 후 이용해주세요.")

def member_login():  #로그인용
    global session

    if session is not None:
        print(f"이미 {names[session]} 님으로 로그인한 사용자입니다.")
        return
    else:
        user_id = input("아이디 : ")
        user_pw = input("비밀번호 : ")

        if user_id in ids:
            idx = ids.index(user_id)
            if not active[idx]: #활성화된 상태가 아니면
                print("비활성화 또는 탈퇴한 계정입니다.")
                return
            else:
                if user_pw == pws[idx]:
                    session = idx
                    print(f"권한 : {groups[idx]}, {names[idx]}님 환영합니다.")
                else:
                    print("비밀번호가 틀렸습니다.")
        else:
            print("존재하지 않는 아이디입니다.")


def member_logout():  #로그아웃
    global session

    if session is None:
        print("로그인 후 이용해주세요.")

    else:
        print(f"{names[session]}님 로그아웃이 완료되었습니다.")
        session = None

def member_modify():  #회원수정
    global session

    if session is None:
        print("로그인 후 이용해주세요.")
        return

    member_modify_menu()
    choice = input(">>> ")

    if choice == "1":
        pws[session] = input("새 비밀번호 : ")
        print("비밀번호 변경 완료")
    elif choice == "2":
        names[session] = input("새 이름 : ")
        print("이름 변경 완료")
    elif choice == "3":
        numbers[session] = input("새 전화번호 : ")
        print("전화번호 변경 완료")
    elif choice == "4":
        print("메인 메뉴로 돌아갑니다.")
    else:
        print("잘못 입력하셨습니다.")


def member_delete():  #회원삭제 및 휴먼계정
    global session

    if session is None:
        print("로그인 후 이용해주세요.")
        return

    member_delete_menu()
    choose = input(">>> ")
    if choose == "1":
        ids.pop(session)
        pws.pop(session)
        names.pop(session)
        groups.pop(session)
        active.pop(session)
        session = None
        print("회원 탈퇴 처리가 완료되었습니다.")

    elif choose == "2":
        active[session] = False
        session = None
        print("휴먼 계정이 활성화되었습니다.")

    else:
        print("잘못 입력하셨습니다.")


# == 메뉴 ==

def main_menu():  #메인메뉴
    print(f"""
=============================================
 MBC 아카데미 회원관리 사이트에 오신것을 환영합니다.   
=============================================

1. 회원가입 | 2. 로그인 | 3. 로그아웃 | 4. 정보수정
5. 회원탈퇴 | 6. 관리자 | 9. 프로그램 종료
    """)

def member_add_menu():
    print(f"""
-----------------------------------------------
         MBC 아카데미 관리자 페이지 입니다.      
-----------------------------------------------
 1. 회원정보 보기 | 2. 권한설정 | 3. 블랙리스트 설정    
 4. 회원 비밀번호 변경 | 5. 블랙리스트 해제 | 6. 뒤로가기
          """)

def member_group_menu():
    print(f"""
---------------------------------
 MBC 아카데미 회원 권한을 선택하세요.          
---------------------------------
1. 관리자 | 2. 매니저 | 3. 일반회원          
    """)

def member_modify_menu():
    print(f"""
--------------------------------------
내 정보 중 수정을 원하시는 번호를 입력하세요.
--------------------------------------
1. 비밀번호 | 2. 이름 | 3. 전화번호 | 4. 뒤로가기
        """)


def member_delete_menu():
    print(f"""
-------------------------------------------
회원 탈퇴 및 휴먼계정 중 원하는 번호를 입력하세요.
-------------------------------------------
      1. 회원 탈퇴 | 2. 휴먼계정 활성화
    
    """)


# == 프로그램 시작 ==
while run:
    main_menu()

    select = input("원하시는 번호를 입력해주세요 >>> ")

    if select == "1":
        member_add()

    elif select == "2":
        member_login()

    elif select == "3":
        member_logout()

    elif select == "4":
        member_modify()

    elif select == "5":
        member_delete()

    elif select == "6":
        member_admin()

    elif select == "9":
        run = False

    else:
        print("원하시는 번호를 정확하게 입력해주세요.")
