# 회원가입과 연동하여 성적처리용 프로그램 개발하기

#필요한 변수
# 학번, 이름, 아이디, 국어점수, 영어점수, 수학점수, 총점, 평균, 등급, 비밀번호, 이메일, 관리자여부

run = True
login_user = None

menu = """
======================
MBC 아카데미 회원 프로그램
======================

1. 회원가입
2. 로그인
3. 회원보기
4. 성적입력
5. 성적보기
6. 성적수정
7. 성적삭제
8. 내 정보 수정
9. 프로그램 종료

"""

sns = []
ids = []
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grades = []
passwords = []
emails = []
admins = [True, False]

while run:
    print(menu)
    select = input("1~9번 중 원하는 메뉴를 입력하세요 : ")

    if select == "1":
        print("회원가입 메뉴에 진입하였습니다.")

        sn = input("사번 : ")
        id = input("아이디 : ")

        if id in ids :
            print("이미 존재하는 아이디 입니다.")
            continue

        pw = input("비밀번호 : ")
        name = input("이름 : ")
        email = input("이메일 : ")

        print("입력 정보 확인")
        print(f"이름 : {name}")
        print(f"아이디 : {id}")
        print(f"이메일 : {email}")

        if input("입력 정보를 확인 했나요? (y/n): ") == "y" :
            sns.append(sn)
            ids.append(id)
            names.append(name)
            emails.append(email)
            passwords.append(pw)
            admins.append(False)
            print("회원가입 완료")
        else :
            print("회원가입 취소")

    elif select == "2" :
        print("로그인 메뉴에 진입하였습니다.")

        id = input("아이디 : ")

        if id in ids :
            idx = ids.index(id)
            pw = input("비밀번호 : ")
            if pw in passwords[idx] :
               print(f"{names[idx]}님 로그인 성공")

               if admins[idx] :
                   print(" > 관리자 계정입니다.")
               else :
                   print(" > 일반 회원입니다.")

            else :
                print("비밀번호를 다시 확인해주세요.")
        else :
            print("아이디를 다시 확인해주세요.")

    elif select == "3" :
        if login_user == None :
            print("로그인 후 이용해주세요.")

        elif admins[login_user] :
            print("전체 회원 확인")
            for i in range(len(ids)) :
                print(f"{i+1}. {names[i]} / {ids[i]} / {emails[i]} / 관리자 : {admins[i]}")

        else :
            print("내 정보 확인")
            print(f"이름 : {names[login_user]}")
            print(f"아이디 : {ids[login_user]}")
            print(f"이메일 : {emails[login_user]}")

    elif select == "4" :
        print("학생 성적을 입력합니다.")

        sn = input("사번을 입력하세요. : ")
        name = input("이름을 입력하세요. : ")
        kor = int(input("국어점수 : "))
        eng = int(input("영어점수 : "))
        mat = int(input("수학점수 : "))
        tot = kor + eng + mat
        avg = tot / 3
        grade = ""

        if avg >= 90 :
            grade = "A"
        elif avg >= 80 :
            grade = "B"
        elif avg >= 70 :
            grade = "C"
        else:
            grade = "F"

        print("입력한 정보를 확인하세요.")
        print(f"사번 : {sn}, 이름 : {name}, 국어 : {kor}, 영어 : {eng}, 수학 : {mat}, 총점 : {tot}, 평균 : {avg}, 등급 : {grade}")

        if input("저장하시겠어요? y : ") == "y" :
            sns.append(sn)
            names.append(name)
            kors.append(kor)
            engs.append(eng)
            mats.append(mat)
            tots.append(tot)
            avgs.append(avg)

            print("저장 완료")
        else :
            print("저장되지 않았습니다.")
            print("처음부터 다시 입력하세요.")

    elif select == "5" :
        print("학생들의 성적을 확인합니다.")
        print("성적목록")

        for i in range(len(sns)) :
            print(f"사번 : {sns[i]} + 이름 : + {name[i]}")
            print(f"국어 : {kor[i]} + \n영어 : {eng[i]} + \n수학 : {mat[i]}")
            print(f"총점 : {tot[i]} + \n평균 : {avg[i]} + \n등급 : {grade[i]}")

    elif select == "6" :
        print("학생들의 성적을 수정합니다.")
        sn = input("성적 수정할 사번 : ")
        if sn in sns :
            print("사번이 존재합니다.")
            snx = sns.index(sn)
            print(f"이름 : {names[snx]}, 국어 : {kors[snx]}, 영어 : {engs[snx]}, 수학 : {mats[snx]}")

            print("점수수정")
            print("1. 국어점수 수정")
            print("2. 영어점수 수정")
            print("3. 수학점수 수정")

            if input("수정할 과목을 선택하세요. : ") == "1" :
                kors[snx] = int(input("국어 점수 수정 : "))
                print("국어 점수 수정 완료 " + kors[snx])
            elif input("수정할 과목을 선택하세요. : ") == "2" :
                engs[snx] = int(input("영어 점수 수정 : "))
                print("영어 점수 수정 완료 " + engs[snx])
            elif input("수정할 과목을 선택하세요. : ") == "3" :
                mats[snx] = int(input("수학 점수 수정 : "))
                print("수학 점수 수정 완료 " + mats[snx])
            else :
                print("점수 변경 취소")

            tot = kors[snx] + engs[snx] + mats[snx]
            avg = tot / 3
            grade = ""

            if avg >= 90 :
                grade = "A"
            elif avg >= 80 :
                grade = "B"
            elif avg >= 70 :
                grade = "C"
            else :
                grade = "F"

            tots[snx] = tot
            avgs[snx] = avg
            grades[snx] = grade

        else :
            print("수정할 사번이 없습니다.")
            print("다시 입력해주세요.")

    elif select == "7" :
        print("학생 성적을 삭제합니다.")
        sn = input("삭제할 사번 : ")

        if sn in sns :
            snx = sns.index(sn)
            print(f"{names[snx]}님의 정보를 삭제합니다.")

            if input("정말 삭제할까요? (y/n): ") == "y" :
                sns.pop(snx)
                names.pop(snx)
                ids.pop(snx)
                emails.pop(snx)
                passwords.pop(snx)
                kors.pop(snx)
                engs.pop(snx)
                mats.pop(snx)
                tots.pop(snx)
                avgs.pop(snx)
                grades.pop(snx)
                admins.pop(snx) # 관리자가 아닌 것을 표시하는 False가 있기 때문에 추가

                print("삭제완료")
            else :
                print("삭제가 취소 되었습니다.")
        else :
            print("학생 정보가 없으므로 처음으로 돌아갑니다.")

    elif select == "8" : #내정보 수정
        if login_user is None :
            print("로그인 후 이용 가능합니다.")
            continue # 로그인 안한 사용자는 하위 코드를 실행하지 않게 하기 위해 사용함.

        print("내 정보 수정")
        print("1. 이름 변경")
        print("2. 이메일 변경")
        print("3. 비밀번호 변경")

        if input("수정할 항목을 선택하세요. : ") == "1" :
            names[login_user] = input("새 이름 : ")
            print("이름 변경 완료 " + names[login_user])

        elif input("수정할 항목을 선택하세요. : ") == "2" :
            emails[login_user] = input("새 이메일 : ")
            print("이메일 변경 완료 " + emails[login_user])

        elif input("수정할 항목을 선택하세요. : ") == "3" :
            passwords[login_user] = input("새 비밀번호 : ")
            print("비밀번호 변경 완료 " + passwords[login_user])

        else :
            print("잘못 선택 하셨습니다.")

    elif select == "9" :
        print("프로그램을 종료합니다.")
        run = False

    else :
        print("1~9번 까지의 숫자를 입력해주세요.")