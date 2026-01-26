# 회원관리용 더미데이터를 파일(메모장)로 저장하여 관리해보자.

import os

# 회원관리 curd를 사용자 지정 함수로 만들어 보자.
# c : 회원가입
# r : 회원리스트 관리자인경우 회원암호 변경, 블랙리스트로생성, 권한 부여
# r : 로그인 id와 pw를 활용하여 로그인 상태 유지 session
# u : 회원정보 수정
# d : 회원탈퇴, 회원비활성화

# 프로그램에서 사용될 변수들
# 전역변수(global) -> py 파일 안에서 전체적으로 사용되는 변수
# 지역변수(local) -> while, if, for, def안에서 사용되는 변수
run = True # while 에서 전체적으로 사용되는 변수(프로그램 구동)
session = None # 로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용
FILE_NAME = "../members.txt"  # 회원 정보를 저장할 메모장 파일명(대문자 : 상수, 변하지 않는 값)
members = []  # 지금은 비어있지만 좀 있다 메모장에 있는 내용을 가져와 리스트 처리함
# members는 2차원 배열로 될 것이다.
# [[  ], [  ], [  ]]
#   0      1     2  ....
# members 구조 :
# [아이디 , 비밀번호, 이름, 권한, 활성화여부]
#    0       1      2     3      4
#                   [아이디 , 비밀번호, 이름, 권한, 활성화여부]
#                                     [아이디 , 비밀번호, 이름, 권한, 활성화여부]

# members[1][3] -> 두번째 회원의 권한을 말함.

# [아이디 , 비밀번호, 이름, 권한, 활성화여부]
#   uid      pw    name   role    active  (변수)
#  "kkw"   "1234" "김기원" "admin" "True"   (값)
#  kkw|1234|김기원|admin|True 로 메모장에 저장될 예정임

# 파일 처리용 함수들!!
def save_members() :  # 메모리 상에 리스트를 파일로 저장함
    """
    members 2차원 리스트 내용을 member.txt 파일에 저장
    """
    with open(FILE_NAME, "w", encoding="utf-8") as f:  # with는 자동으로 close를 실행
        #     상수     덮어쓰기         한글처리용     파일객체(파일이 들어있는 변수)
        #                 a = 추가용
        # 메모리에 있는 리스트를 |로 연결하여 한줄로 저장
        for member in members :  # members는 메모리에 있는 2차원 배열
            line = f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}\n"
            #                kkw|       1234|      김기원|      admin|       True
            f.write(line)
# save_members() 함수 종료

def load_members() :   # 텍스트 파일을 전체 불러와 리스트로 만듬 - 왜? - 중간수정이 안됨
    """
    member.txt 파일을 읽어서 members 리스트에 저장
    """

    # 파일이 없으면 새파일 생성(암기)

    if not os.path.exists(FILE_NAME):  #지금 디렉토리에 FILE_NAME이 없으면
        # os.path 는 현재 위치 (os:윈도우 운영체제)
        # os는 내부 라이브러리지만 기본적으로 포함되지 않아 import 해야함
        save_members()   # 빈 파일이 members.txt로 생성됨
        # with open(FILE_NAME,"w","encoding="utf-8")as f:
        return

    # 파일이 있으면 열어서 한줄 씩 읽기를 해야함.
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        #     member.txt 읽기전용        한글지원    f라는 변수에 넣어
        for line in f:   # f 파일내용을 한줄씩 line 변수에 넣음
            #print(f"변조전 데이터 : {line}")
            # kkw|1234|김기원|admin|True

            # 줄 끝에 엔터 제거, |로 분류된 것 리스트화
            data = line.strip().split("|")
            #           맨뒤에 엔터 제거
            #                    |를 기준으로 나눔

            # 변조 후 데이터를 확인해보면 모두 다 문자열로 취급됨.
            # 문자열 True를 블리언 타입으로 변환
            # 블리언타입 : True, False
            data[4] = True if data[4] == "True" else False  # 이 함수는
            # 받은변수    넣을 값    data4번째  가 문자열 True 이면
            #                                   아니면 False 를 넣음
            # if data[4] == "True" :
            #    data[4] = True
            # else :
            #     data[4] = False
            # 라는 뜻의 함수임
            #print(f"변조 후 데이터 : {data}")
            print("------------------------")

            # 마지막 members 리스트에 넣는다.
            members.append(data)
# load_members() 함수 종료



# 프로그램에서 사용될 함수들
def member_add():
    # 회원가입용 함수
    #print("member_add 함수로 진입합니다.")
    # 회원가입에 필요한 기능을 넣음
    print("회원가입 페이지입니다.")
    uid = input("아이디 : ")

    # 아이디 중복검사
    for member in members :
        if member[0] == uid: # {member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]
            #                      uid        pw          name        role        active
            print("이미 존재하는 아이디 입니다.")
            return # 돌아감 -> 함수를 빠져나와 메인메뉴로 돌아감
            # return을 걸었기 때문에 else처리 안해도 됨

    # else 처리 없이 return으로 처리함
    pw = input("비밀번호 : ")
    name = input("이름 : ")

    # 권한 선택
    # print("1. admin  2.manager  3.user ")
    # roleSelect = input("권한 선택 : ")
    #
    role = "user" # 잘못 클릭해도 user권한으로 기본값
    # if roleSelect == "1":
    #     role = "admin"
    # elif roleSelect == "2":
    #     role = "manager"

    # ====== 입력 종료 =======
    print(f"아이디 : {uid}  이름 : {name} ")
    print(f"권한 : {role}    암호 : {pw} ")
    # ====== 입력값 확인

    save_True = input("저장하려면 y를 누르세요 :")
    if save_True == "y" :
        # 저장 시작!!!
        members.append([uid, pw, name, role, True]) # 리스트로 만듬
        save_members() # 리스트를 파일에 저장
        print("회원가입완료")

    else:
        print("회원가입이 완료되지 않았습니다. 다시 시도해주세요.")

# member_add() 함수 종료

    #print("member_add 함수를 종료합니다.")
# 회원가입용 함수 종료

def member_login() :
    # 가입된 회원을 확인하여 로그인 처리 후 session 변수에 인덱스를 넣음
    #print("member_login 함수로 진입합니다.")
    print("로그인 페이지입니다.")
    # 로그인에 필요한 기능을 넣음

    global session  # 전역변수로 생성한 값을 가져옴(이미 로그인한 상태? or None = 로그인안한상태)
    #                                               인덱스

    if session is not None:
        print(f"이미 {members[session][2]}님으로 로그인한 사용자입니다.")
        return

    uid = input("아이디 : ")
    pw = input("비밀번호 : ")  # 키보드로 아이디와 비밀번호 입력하고 변수에 넣음

    # 회원 목록에서 아이디 검색
    for idx, member in enumerate(members) :
        # enumerate()는 for문(반복문)으로 인덱스를 찾아옴
        # idx = 1차원 주소
        # member -> 2차원 리스트
        print("idx : ", idx)  # idx -> 1차원 주소
        print("member : ", member)  # member -> 2차원 리스트
        #print 하면 이런식으로 아래처럼 결과가 나옴
        # idx: 0
        # member: ['kkw', '1234', '김기원', 'admin', True]
        # idx: 1
        # member: ['lhj', '4321', '임효정', 'manager', True]
        # idx: 2
        # member: ['ljj', '2345', '이재정', 'user', True]

        if member[0] == uid:  # 키보드로 입력한 uid와 리스트에 있는 값이 같으면 아이디 찾음
            if not member[4] :  # active 상태 확인(False이면)
                print("로그인 할 수 없는 계정입니다.(블랙리스트/비활성화)")
                return  # 로그인 중단 member_login() 함수로 종료

            # 비밀번호 확인
            if member[1] == pw:  # 키보드로 입력한 암호화 리스트[1]의 암호가 같으면
                session = idx  # 전역변수에 로그인한 주소를 넣음
                print(f"{member[2]}님 로그인 성공")
                print(f"{member[3]} 권한으로 로그인 되었습니다.")

                #if member[3] == "admin":
                    #member_admin()
                return   # return을 쓰면 for문을 빠져나옴(member_login()함수 종료)

            else:
                print("비밀번호가 틀렸습니다. 메인메뉴로 이동합니다.")
                return

        # else:   예외 발생 가능성이 있음. for로 찾으면서 없으면 출력이 되기 때문
        #     print("찾는 아이디가 없습니다.")

    print("존재하지 않는 아이디입니다.")  # for문이 돌다가 찾는 값이 return에 없으면 출력되는 값


    #print("member_login 함수를 종료합니다.")
# 회원로그인용 함수 종료

def member_admin() :
    # 관리자가 로그인 했을 경우 할수 있는 기능을 작성
    #print("member_admin 함수로 진입합니다.")

    global session

    if members[session][3] == "manager":
        selid = input("정보 변경 하실 아이디 : ")
        manager_menu()

        choice1 = input("원하는 번호 선택 : ")
        #print("admin")

        print(members[session][0])

        if selid == members[0][0]:
            # 만약 내가 admin인 사람의 인덱스 정보를 알고 있을 때

            #아래의 문구는 미완성
            # for idx,member in enumerate(members):
            #     if member[0] == selid:
            #         if member[3] == 'admin':
            print("매니저는 관리자 정보를 수정할 수 없습니다.")
            return

            # print("관리자는 관리자 외 다른 권한으로 변경할 수 없습니다.")
            # return
        if selid == members[2][0]:
            #만약 내가 manager인 사람의 인덱스 정보를 알고 있을 때

            print("매니저는 매니저 정보를 수정할 수 없습니다.")
            return


        for member in members:
            if member[0] == selid:

                if choice1 == "1":  # 다른 사용자 암호 변경 코드
                    print("\n[회원 비밀번호 변경]")
                    member[1] = input("변경할 비밀번호 : ")
                    print("비밀번호가 변경되었습니다.")
                    print("해당회원에게 로그인 후 비밀번호를 변경하라고 안내해주세요.")
                    save_members()
                    return

                elif choice1 == "2":  # 블랙리스트로 변환 -> active를 False
                    print("\n[블랙리스트 등록]")
                    member[4] = False
                    member[3] = "blacklist"
                    print(f"블랙리스트로 등록되었습니다. {selid}님은 사용이 제한됩니다.")
                    save_members()
                    return

                elif choice1 == "3":  # 일반 사용자로 변환 -> active를 True
                    print("\n[블랙리스트 해제]")
                    print("블랙리스트 해제시 일반 사용자로 권한이 변경됩니다.")
                    member[4] = True
                    member[3] = "user"
                    print(f"{selid}님의 블랙리스트 해제가 완료되었습니다.")
                    save_members()
                    return

                else:
                    print("처음으로 돌아갑니다.")
                    return

    # if members[session][3] == "manager" or members[session][3] == "user":
    #     print("관리자로 로그인 후 이용가능합니다. ")
    #     return
    #
    print("admin")
    if members[session][3] != "admin":
        print("관리자로 로그인 후 이용가능합니다. ")
        return


    print("관리자 페이지 입니다.")

    selid = input("정보 변경 하실 아이디 : ")

    print("1. 회원 비밀번호 변경")
    print("2. 블랙리스트 등록")
    print("3. 블랙리스트 해제")
    print("4. 권한 변경")

    choice = input("원하는 번호 선택 : ")


    for member in members :
        if member[0] == selid :

            if choice == "1": # 다른 사용자 암호 변경 코드
                print("\n[회원 비밀번호 변경]")
                member[1] = input("변경할 비밀번호 : ")
                print("비밀번호가 변경되었습니다.")
                print("해당회원에게 로그인 후 비밀번호를 변경하라고 안내해주세요.")
                save_members()
                return

            elif choice == "2": # 블랙리스트로 변환 -> active를 False
                print("\n[블랙리스트 등록]")
                member[4] = False
                member[3] = "blacklist"
                print(f"블랙리스트로 등록되었습니다. {selid}님은 사용이 제한됩니다.")
                save_members()
                return

            elif choice == "3": # 일반 사용자로 변환 -> active를 True
                print("\n[블랙리스트 해제]")
                print("블랙리스트 해제시 일반 사용자로 권한이 변경됩니다.")
                member[4] = True
                member[3] = "user"
                print(f"{selid}님의 블랙리스트 해제가 완료되었습니다.")
                save_members()
                return

            elif choice == "4": # 권한 부여 -> 사용자의 권한roles를 변경 (manager <-> user)
                print("\n[권한 변경]")

                if member[3] == "admin":
                    print("관리자는 관리자 외 다른 권한으로 변경할 수 없습니다.")
                    return

                member_add_menu()
                choose = input("변경할 권한 번호 선택 : ")

                # if choose == "1":
                #     member[3] = "admin"
                #     print("관리자 권한으로 변경되었습니다.")

                if choose == "1":
                    member[3] = "manager"
                    print("매니저 권한으로 변경되었습니다.")

                elif choose == "2":
                    member[3] = "user"
                    print("일반사용자 권한으로 변경되었습니다.")

                save_members()
                print("회원 정보 변경 완료")
                return

            else:
                print("원하시는 번호를 정확하게 입력해주세요.")
                return

    else:
        print("찾으시는 회원 아이디가 존재하지 않습니다.")
        return
#    print("member_admin 함수로 종료합니다.")
# 관리자가 사용자 변경사항 함수 종료

def member_logout() :
    # 회원 로그아웃으로 상태 변경 -> session 값을 None으로 변경
    #print("member_logout 함수로 진입합니다.")
    print("로그아웃 페이지입니다.")

    global session

    if session is None :
        print("로그인 후 이용해주시길 바랍니다.")
        return

    else:
        print(f"{members[session][2]}님 로그아웃이 완료되었습니다.")
        session = None

    # 로그인 상태인지를 확인하고 session을 None으로 변경

    #print("member_logout 함수를 종료합니다.")
# 로그아웃 함수를 종료

def member_modify():
    # 회원 정보 수정
    #print("member_modify 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 자산의 정보를 확인하고 수정한다.

    global session

    if session is None :
        print("로그인 후 이용해주세요.")
        return


    print("회원 정보 수정 페이지입니다.")

    print("\n1. 이름 변경")
    print("2. 비밀번호 변경")
    print("3. 아이디 변경")

    change = input("수정하고 싶은 번호를 입력해주세요 : ")

    if change == "1":
        members[session][2] = input("변경할 이름 : ")
        print("이름 변경 완료")
    elif change == "2":
        members[session][1] = input("변경할 비밀번호 : ")
        print("비밀번호 변경 완료")
    elif change == "3":
        uid = input("변경할 아이디 : ")
        # 현재 로그인한 사용자가 아이디를 변경할때
        # 현재 가입되어있는 사용자의 아이디와 같은지 비교해서 중복되면
        # 변경이 안되게 하려면 uid라는 변수를 두고 member[0]에 있는 아이디들과
        # 변경하려는 아이디와 비교 후 같은게 있으면 존재하는 아이디라 뜨게하고
        # 변경하려는 아이디와 같은 아이디가 없으면 변경 완료라고 뜨게 하는 함수사용
        for member in members :
            if member[0] == uid:
                print("이미 존재하는 아이디입니다.")
                return

        # 변경하려는 아이디와 같은 아이디가 없을 경우 uid를 현재 로그인한 사용자의 아이디로 변경하는 방법
        members[session][0] = uid
        print("아이디 변경 완료")

    save_members()

    #print("member_modify 함수를 종료합니다.")
# 회원정보 수정 종료

def member_delete():
    # 회원 탈퇴 또는 회원 유휴등 처리
    #print("member_delete 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 탈퇴는 pop, 유휴(active=False)

    global session

    if session is None:
        print("로그인 후 이용해주세요.")
        return

    print("회원 탈퇴 및 휴먼 설정 페이지입니다.")

    print("\n1. 회원 탈퇴 하기")
    print("2. 휴먼(비활성화) 계정 설정하기")

    c = input("원하시는 번호를 입력해주세요 : ")

    if c == "1":
        print("회원 탈퇴 후에는 복구가 어려우니 신중하게 선택해주세요.")
        print("정말 회원을 탈퇴하시겠습니까? (y/n)")

        s = input(">>> ")

        if s == "y":
            members.pop(session)
            session = None
            members.pop
            print("회원 탈퇴 처리가 완료되었습니다.")
        else:
            print("회원 탈퇴를 취소하였습니다.")
            return

    elif c == "2":
        print("휴먼 설정 후 계정을 복구하시려면 관리자에게 문의해주세요.")
        members[session][4] = False
        print("휴먼 계정이으로 변경되었습니다.")

    save_members()

    #print("member_delete 함수를 종료합니다.")
# 회원탈퇴 종료

# --------------------- 기능에 대한 함수 생성 끝----------------

def main_menu() :
    print(f"""
    ==== 엠비씨아카데미 회원관리 프로그램입니다======
    1. 회원가입       2. 로그인        3. 로그아웃
    4. 회원정보수정      5. 회원탈퇴      6. 관리자
    9. 프로그램 종료
    """)
# 메인메뉴용 함수 종료

def member_add_menu() : # 회원가입에서 사용할 메뉴
    print(f"""
    ------- 회원권한을 확인하세요.-------
       1. 매니저        2. 일반사용자 
    """)

def manager_menu():
    print(f"""
    ------------- 매니저 메뉴 -------------
    1. 회원 비밀번호 변경   2. 블랙리스트 등록 
    3. 블랙리스트 해제   
    """)


# ------------------ 메뉴 함수 끝 ------------------



# 프로그램 시작!!!!

load_members()   # 프로그램 시작 시 파일을 불러오기 -> 1번만 2차원 배열로 불러옴
print(members)

while run : # 메인 프로그램 실행 코드
    main_menu() # 위에서 만든 메인 메뉴함수를 실행

    if session == None:
        print("현재 비로그인 상태입니다. 로그인 하려면 2번을 입력하세요.")
        print("회원이 아니면 1번을 입력하세요.")
    else:
        print(f"{members[session][2]}님 환영합니다.")


    select = input(">>>") # 키보드로 메뉴 선택
    if select == "1" : # 회원가입 코드
        member_add()   # 회원가입용 함수 호출

    elif select == "2" : # 로그인 메뉴 선택
        member_login() # 로그인용 함수 호출

    elif select == "3" : # 로그아웃 메뉴 선택
        member_logout() # 로그아웃 함수 호출

    elif select == "4" : # 회원정보 수정 선택
        member_modify()  # 회원정보 수정 함수 호출

    elif select == "5" : # 회원탈퇴 선택
        member_delete()     # 회원정보 삭제 함수 호출

    elif select == "6" : # 관리자메뉴
        member_admin()

    elif select == "9" : # 프로그램 종료 선택
         run = False

    else:
        print("잘못 입력하셨습니다.")
# while문 종료