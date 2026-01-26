# 대부분 프로그래밍에서 1번이 되는(start) 파일을 main으로 만든다.
# 프로그램을 만들때는 목표를 가지고 써내려 가기.
# 목표 : MBC아카데미 LMS 프로그램을 만들어보자. (LMS : 학사관리 프로그램)
# 출결상황, 성적, 장학금, 학점관리, 등록금 납부관리 등 (학생)
# 학점등록, 학생관리, 성적관리 등 (교수)

# 회원관리 : 시스템 담당자, 교수, 행정직원, 학생, 손님, 학부모
# 성적관리 : 교수 : 성적 등록, 수정,
#          행정 담당자 : 1년에 한번 또는 학기마다 백업(이전 -> 삭제)
#          학생 : 개인성적 열람, 성적 출력
#          손님 : 학교 소개 페이지 열람
#          학부모 : 자녀 학사 관리
# 게시판 : 회원제, 비회원제, 문의사항, Q/A
# 시스템 담당자 : 게시판 프로그램 이상 시 보수

# 필요한 변수
run = True   # 메인 메뉴용 while
# subRun = True   # 보조 메뉴용 while (실행을 돌리면 서브메뉴가 안나오기때문에 주석처리함)
session = None   # 로그인한 사용자의 인덱스를 기억하는 변수

# 필요한 리스트

# 회원에 대한 리스트
sns = [1]   # 회원에 대한 번호
ids = ["kkw"]   # 아이디에 대한 리스트
pws = ["1234"]   # 암호에 대한 리스트
group = ["admin"]   # 회원 등급  (admin, professor, student, normal)
names = ["관리자"]
emails = ["admin@mbc.com"]
# admin(관리자), stu(학생), guest(손님)

# 성적에 대한 리스트
python_score = []   # 파이썬 점수들
dataBaseScore = []   # 데이터베이스 점수들
wwwScore = []   # 프론트 점수들
totalScore = []    # 총점들
avgScore = []    # 평균들
gradeScore = []    # 등급들
stuIdx = []    # 학생의 인덱스(학번) <-> 회원의 번호(sns)

# 게시판에 대한 리스트
board_no = []   # 게시물의 번호
board_title = []    # 게시물의 제목
board_content = []    # 게시물의 내용
board_writer = []   # 게시물의 작성자 <-> 회원의 번호(sns)
board_hit = []   # 좋아요 수
board_visitcount = []   # 조회수
# 로그인했을때 session 이용해서 연동시키기

# 메뉴 구성
mainMenu = """
===================================
MBC 아카데미 LMS에 오신 것을 환영합니다.
===================================

1. 로그인(회원가입)
2. 성적관리
3. 게시판
4. 관리자메뉴
9. 프로그램 종료

"""

memberMenu = """
-----------------
회원 관리 메뉴입니다.
-----------------

1. 로그인
2. 회원가입
3. 회원수정
4. 회원탈퇴

9. 회원 관리 메뉴 종료

"""

scoreMenu = """
------------------
성적 관리 메뉴입니다.
------------------

1. 성적 입력(교수 전용)
2. 성적 보기(개인용)
3. 성적 수정(교수 전용)
4. 성적 백업(행정 직원 전용)

9. 성적 관리 메뉴 종료

"""

boardMenu = """
------------------
회원제 게시판 입니다.
------------------

1. 게시글 등록
2. 게시글 전체보기
3. 게시글 자세히보기
4. 게시글 수정
5. 게시글 찾기
6. 게시글 삭제

9. 회원제 게시판 메뉴 종료

"""

# 주 실행문 구현

while run:
    print(mainMenu)   # 메인메뉴 출력용
    select = input(">>>")   # 사용자가 주메뉴 선택 값을 select 넣는다.

    if select == "1":
        print("로그인(회원가입) 메뉴로 진입합니다.")

        subRun = True

        while subRun:   # 부메뉴 반복용
            print(memberMenu)   # 회원관리 메뉴가 출력

            subSelect = input(">>>")   # 회원 부메뉴 선택값을 subselect에 넣음

            if subSelect == "1":   #로그인
                print("로그인 메뉴로 진입합니다.")

                id = input("아이디 : ")
                pw = input("비밀번호 : ")

                if id in ids :
                    idx = ids.index(id) # 주소값
                    if pws[idx] == pw:
                        session = idx
                        print(f"{ids[idx]}님 로그인 성공")

                        if group[idx] == "admin" :
                            print(" > 관리자 계정입니다.")
                        elif group[idx] == "professor" :
                            print(" > 교수 계정입니다.")
                        else :
                            print(" > 일반회원 계정입니다.")
                        subRun = False
                    else :
                        print("비밀번호가 틀렸습니다.")
                else :
                    print("존재하지 않는 아이디입니다.")

            elif subSelect == "2":   # 회원가입
                print("회원가입 메뉴로 진입합니다.")

                sn = input("학번 : ")
                id = input("아이디 : ")

                if id in ids :
                    print("이미 존재하는 아이디입니다.")
                    continue

                pw = input("비밀번호 : ")
                name = input("이름 : ")
                email =input("이메일 : ")

                # 관리자, 교수, 일반회원 구분

                print("1. 관리자")
                print("2. 교수")
                print("3. 학생")
                print("4. 일반회원")

                number = input("가입 시 해당하는 회원 유형을 입력하세요 : ")

                if number == "1":
                    group.append("admin")
                    print("관리자 계정이 생성되었습니다.")
                elif number == "2":
                    group.append("professor")
                    print("교수 계정이 생성되었습니다.")
                elif number == "3":
                    group.append("student")
                    print("학생 계정이 생성되었습니다.")
                elif number == "4":
                    group.append("normal")
                    print("일반 회원 계정이 생성되었습니다.")
                else: # 1~3 외 값 방어용코드
                    print("1~4번 중 원하시는 입력해주세요")
                    continue

                # 입력한게 맞는지 정보 확인

                print("\n[입력 정보 확인]")
                print(f"이름 : {name}")
                print(f"아이디 : {id}")
                print(f"이메일 : {email}")
                print(f"회원등급 : {group}")

                if input("가입하시겠습니까? (y/n) : ") == "y":
                    sns.append(sn)
                    ids.append(id)
                    names.append(name)
                    pws.append(pw)
                    emails.append(email)
                    print("회원가입이 완료되었습니다.")
                else :
                    print("회원가입이 취소되었습니다.")

            elif subSelect == "3":   # 회원수정
                if session is None :
                    print("로그인 후 이용 가능합니다.")
                else:
                    print("회원수정 메뉴로 진입합니다.")
                    print("\n[내 정보 수정]")
                    print("1. 이름 수정")
                    print("2. 비밀번호 수정")
                    print("3. 이메일 수정")

                    choice = input("수정을 원하시는 번호를 입력해주세요. : ")

                    if choice == "1":
                        names[session] = input("새 이름 : ")
                        print("이름 변경 완료 : " + names[session])
                    elif choice == "2":
                        pws[session] = input("새 비밀번호 : ")
                        print("비밀번호 변경 완료 : " + pws[session])
                    elif choice == "3":
                        emails[session] = input("새 이메일 : ")
                        print("이메일 변경 완료 : " + emails[session])
                    print(f"이름 : {names[session]} / 비밀번호 : {pws[session]} / 이메일 : {emails[session]}")

            elif subSelect == "4":   # 회원탈퇴
                if session is None :
                    print("로그인 후 이용해주세요.")
                    continue

                elif session in ids :
                    print("회원탈퇴 메뉴로 진입합니다.")

                    sn = input("삭제할 학번 : ")

                    if sn in sns :
                        snx = sns.index(sn)
                        print(f"{names[snx]}님의 정보를 삭제합니다.")

                        if input("정말 삭제할까요? (y/n) : ") == "y" :
                            sns.pop(snx)
                            ids.pop(snx)
                            pws.pop(snx)
                            names.pop(snx)
                            emails.pop(snx)
                            group.pop(snx)

                            print("회원 탈퇴가 완료되었습니다.")
                        else :
                            print("회원 탈퇴를 취소합니다.")
                    else :
                        print("탈퇴할 회원 정보가 없으므로 처음으로 돌아갑니다.")


            elif subSelect == "9":
                print("회원관리 메뉴를 종료합니다.")
                subRun = False

            else :   # 1,2,3,4,9 말고 다른 키를 넣을 경우
                print("잘못된 메뉴를 선택하셨습니다.")

    elif select == "2":
        print("성적관리 메뉴로 진입합니다.")

        subRun = True

        while subRun:
            print(scoreMenu)

            subselect = input(">>>")

            if subselect == "1":   # 성적입력
                if session is None :
                    print("관리자로 로그인 후 이용해주세요.")
                    continue

                elif group[session] == "professor" :
                    print(f"{names[idx]}교수님 성적 입력 메뉴에 진입하였습니다.")

                    sn = int(input("학번 : "))
                    name = int(input("이름 : "))
                    python = int(input("파이썬 점수 : "))
                    dataBase = int(input("데이터베이스 점수 : "))
                    www = int(input("프론트 점수 : "))
                    tot = python + dataBase + www
                    avg = tot / 3

                    grade = None

                    if avg >= 90 :
                        grade = "A"
                    elif avg >= 80 :
                        grade = "B"
                    elif avg >= 70 :
                        grade = "C"
                    else:
                        grade = "F"

                    print("입력한 정보를 확인하세요.")
                    print(f"학번 : {sn}, 이름 : {name}, 파이썬 : {python}, 데이터베이스 : {dataBase}, 프론트 : {www}, 총점 : {tot}, 평균 : {avg}, 등급 : {grade} ")

                    if input("저장하시겠습니까? (y/n) : ") == "y":
                        stuIdx.apeend(sn)
                        python_score.append(python)
                        dataBaseScore.append(dataBase)
                        wwwScore.append(www)
                        totalScore.append(tot)
                        avgScore.append(avg)
                        gradeScore.append(grade)

                        print("저장이 완료되었습니다.")

                    else :
                        print("저장되지 않았습니다.")
                        print("처음부터 다시 입력해주세요.")

                else:
                    print("권한이 없습니다.")


            elif subSelect == "2":    # 성적보기
                if session is None:
                    print("로그인 후 이용해주세요.")
                    continue
                else:
                    # 전체 성적 보기  **모르겠음@@@!!!!!!
                    if group[session] == "admin" and group[session] == "professor" :
                        print("성적 전체 보기 메뉴에 진입하였습니다.")
                        print("\n[성적 목록]")

                        for i in range(len(sns)):
                            print(f"학번 : {sns[i]} + 이름 : {names[i]}")
                            print(f"파이썬 : {python_score[i]} + \n데이터베이스 : {dataBaseScore[i]} + \n프론트 : {wwwScore[i]}")
                            print(f"총점 : {totalScore[i]} + \n평균 : {avgScore[i]} + \n등급 : {gradeScore[i]}")

                        # 관리자나 교수일 경우 continue 사용해서 끝맺고싶은데????? 이게맞나
                        #for i in range(len(sns)):
                        #    if group[i] == "admin" or group[i] == "professor" :
                        #        continue

                        # 개인 성적 보기
                    elif group[session] == "normal" :
                        print("내 성적 보기 메뉴에 진입하였습니다.")

                        snq = input("학번으로 검색하기 : ").lower()
                        found = False

                        if snq in sns :
                            print("학번이 존재합니다.")

                            for i in range(len(sns)):
                                if sn in names[i].lower() :
                                    print(f"{sns[i]}|t{names[i]}|t{python_score[i]}|t{dataBaseScore[i]}|t{wwwScore[i]}|t{totalScore[i]}|t{avgScore[i]}|t{gradeScore}")
                                    found = True

                        if not found :
                            print("학번이 존재하지 않습니다.")

            elif subSelect == "3":   # 성적 수정
                if session is None:
                    print("관리자로 로그인 후 이용해주세요.")
                    continue

                elif group[session] == "admin" or group[session] == "professor":
                    print("성적 수정 메뉴에 진입하였습니다.")

                    sn = input("성적 수정할 학번 : ")

                    if sn in sns :
                        print("학번이 존재합니다.")
                        snx = sns.index(sn)
                        print(f"학번 : {sns[i]}, 이름 : {names[i]}")

                        print("[성적 수정]")
                        print("1. 파이썬 점수 수정")
                        print("2. 데이터베이스 점수 수정")
                        print("3. 프론트 점수 수정")

                        if input("수정할 과목을 선택하세요 : ") == "1" :
                            python_score[snx] = int(input("파이썬 점수 수정 : "))
                        elif input("수정할 과목을 선택하세요 : ") == "2" :
                            dataBaseScore[snx] = int(input("데이터베이스 점수 수정 : "))
                        elif input("수정할 과목을 선택하세요 : ") == "3" :
                            wwwScore[snx] = int(input("프론트 점수 수정 : "))
                        else :
                            print("점수 변경을 취소합니다.")
                    else :
                        print("수정할 항목이 선택되지 않았습니다.")
                        print("처음으로 돌아갑니다.")

            elif subSelect == "4" :  # 성적 백업
                if session is None:
                    print("관리자로 로그인 후 이용해주세요.")
                    continue

                elif group[session] == "admin" :
                    print("성적 백업 메뉴에 진입하였습니다.")

                    sn = input("성적 삭제할 학번 : ")

                    if sn in sns :
                        snx = sns.index(sn)
                        print(f"{names[snx]}님의 성적을 삭제합니다.")

                        if input("정말 삭제할까요? (y/n) : ") == "y" :
                            sns.pop(snx)
                            names.pop(snx)
                            ids.pop(snx)
                            pws.pop(snx)
                            group.pop(snx)
                            emails.pop(snx)
                            python_score.pop(snx)
                            dataBaseScore.pop(snx)
                            wwwScore.pop(snx)
                            totalScore.pop(snx)
                            avgScore.pop(snx)
                            gradeScore.pop(snx)
                            print("삭제가 완료되었습니다.")
                        else :
                            print("삭제가 취소되었습니다.")
                    else :
                        print("학번 정보가 없으므로 처음으로 돌아갑니다.")

            elif subSelect == "9":
                print("성적 관리 메뉴를 종료합니다.")
                run = False

            else :
                print("잘못된 번호를 선택하셨습니다.")


    elif subSelect == "3":

        if session is None:
            print("로그인 후 이용해주세요.")
            continue

            # session = board_writer ??

        print("회원제 게시판 메뉴로 진입합니다.")

        subRun = True

        while subRun :
            print(boardMenu)   # 게시판 메뉴 출력

            subselect = input(">>>")

            if subselect == "1":   # 게시글 등록
                print("게시글 등록 메뉴에 진입하였습니다.")

                title = input("제목 : ")
                content = input("내용 : ")
                writer = input("작성자 : ") # 연동을 어떻게시키지

                print(f"제목 : {title}, 내용 : {content}, 작성자 : {writer}")

                choose = input("위 내용으로 저장하시겠습니까? (y/n) : ")

                if choose == "y" :
                    board_title.append(title)
                    board_content.append(content)
                    board_writer.append(writer)

                    no = len(board_no) + 1
                    board_no.append(no)
                    board_hit.append(0)
                    board_visitcount.append(0)

                    print(f"{no}번의 게시글이 등록되었습니다.")
                else :
                    print("게시글이 저장되지 않았습니다.")
                    print("처음으로 돌아갑니다.")

            elif subselect == "2":   # 게시글 전체보기
                print("게시글 전체 보기 메뉴에 진입하였습니다.")

                print("===================================")
                print("번호\t제목\t작성자\t조회수")
                print("===================================")

                if len(board_no) == 0 :
                    print("작성된 게시글이 없습니다.")
                    continue
                for i in range(len(board_no)) :
                    print(f"{board_no[i]}\t{board_title}\t{board_writer}\t{board_visitcount[i]}")

            elif subselect == "3":   # 게시글 자세히보기
                print("게시글 자세히보기 메뉴에 진입하였습니다.")

                bno = int(input("자세히 볼 게시글 번호 : "))

                if bno in board_no :
                    print("게시글을 찾았습니다.")

                    idx = board_no.index(bno)
                    board_visitcount[idx] += 1

                    print("======================================")
                    print(f"번호 : {board_no[idx]}")
                    print(f"제목 : {board_title[idx]}")
                    print(f"내용 : {board_content[idx]}")
                    print(f"작성자 : {board_writer[idx]}")
                    print(f"조회수 : {board_visitcount[idx]}")
                    print(f"좋아요 : {board_hit[idx]}")
                    print("======================================")

                    if input("좋아요를 누르시겠습니까? (y/n) : ") == "y" :
                        board_hit[idx] += 1
                        print("좋아요를 눌렀습니다.")
                    else :
                        print("다음엔 더 유익한 게시글이 되기를 바랍니다.")
                else :
                    print("찾는 게시글이 없으므로 처음으로 돌아갑니다.")

            elif subselect == "4":   # 게시글 수정하기
                print("게시글 수정하기 메뉴에 진입하였습니다.")

                bno = int(input("수정할 게시글 번호 : "))

                if bno in board_no :
                    print("수정할 게시글을 찾았습니다.")
                    idx = board_no.index(bno)
                    print(f"제목 : {board_title[idx]}, 내용 : {board_content[idx]}, 작성자 : {board_writer[idx]}")

                    print("[게시글 수정]")
                    print("1. 제목 수정")
                    print("2. 내용 수정")

                    choose = input("수정할 항목의 번호를 입력하세요. : ")

                    if choose == "1" :
                        board_title[idx] = input("제목 수정 : ")
                        print("제목 : " + board_title[idx] + "로 수정되었습니다.")
                    elif choose == "2" :
                        board_content[idx] = input("내용 수정 : ")
                        print("내용 : " + board_content[idx] + "로 수정되었습니다.")
                    else :
                        print("수정이 취소되었습니다.")
                else :
                    print("수정할 항목이 입력되지 않았습니다.")

            elif subselect == "5":   # 게시글 찾기
                print("게시글 찾기 메뉴에 진입하였습니다.")

                print("[게시글 검색]")
                print("1. 제목으로 검색")
                print("2. 작성자로 검색")

                #choose =



            #elif subselect == "6":   # 게시글 삭제하기



            elif subselect == "9":   #게시판 프로그램 종료하기
                print("회원제 게시판 메뉴를 종료합니다.")
                run = False
            else :
                print("잘못된 번호를 선택하셨습니다.")
                print("처음으로 돌아갑니다.")

    #elif subSelect == "4":   # 관리자 메뉴

    #elif subselect == "9":   # LMS 프로그램 종료


    else :
        print("원하시는 항목의 숫자를 입력해주세요.")
