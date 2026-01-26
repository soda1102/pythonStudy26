# 비회원용 게시판을 만들어보자.

# 프로젝트 목표

# C : 게시글 등록
# R : 게시글 전체 보기(리스트) / 게시글 자세히보기
# U : 게시글 수정
# D : 게시글 삭제

# 사용할 변수 리스트

run = True  # while문 프로그램 구동중일때 사용

# 프로그램 전반적으로 사용하는 변수 (전역변수)
board_no = []   # 중복되지 않는 유일한 값, 공백X(not null)
board_title = []   # 게시글 제목
board_content = []   # 게시글 내용
board_writer = []   # 글쓴이
board_password = []  # 게시글의 암호(수정, 삭제용)
board_hit = []  # 좋아요
board_visitcount = []   # 조회수

# 주메뉴
menu = """
==============================
엠비씨 아카데미 비회원 게시판입니다.
==============================

1. 게시글 등록하기
2. 게시글 리스트 보기
3. 게시글 자세히 보기
4. 게시글 수정하기
5. 게시글 삭제하기
6. 게시판 프로그램 종료

"""

# 프로그램 실행문
while run:
    print(menu)
    # select 변수는 while문 안에서만 사용가능. 들여쓰기가 끝나면 사용X, 1회성 (지역변수)
    select = input("1~6번 중 원하는 메뉴를 입력하세요. : ")

    # input은 키보드로 입력한 값을 문자열로 전달하기 때문에 ""를 사용함.
    if select == '1':   # 키보드로 입력한 값이 1이면?
        print("게시글 등록하기 탭에 진입하였습니다.")
        # 게시글 등록용 코드 추가

        # 게시글의 번호는 프로세스가 자동처리
        # 키보드로 게시글을 받아 변수에 넣는다.
        title = input("제목을 입력해주세요. : ")
        content = input("내용을 입력해주세요. : ")
        writer = input("작성자를 입력해주세요. : ")
        password = input("암호를 입력해주세요. : ")

        # 넣은 정보를 확인한다.
        print(f"제목 : {title}, 내용 : {content})")
        print(f"작성자 : {writer}, 암호 : {password}")

        choose = input("저장하려면 y를 누르세요. : ")

        if choose == 'y':
            board_title.append(title)   # 제목 추가
            board_content.append(content)   # 내용 추가
            board_writer.append(writer)   # 작성자 추가
            board_password.append(password)    # 암호 추가

            # 제목의 리스트에서 인덱스를 추출하여 + 1한 값이 no
            # 아래 함수는 제목이 중복되면 같은 번호로 들어가는 문제 발생
            #for idx in range(len(board_title)):  # range 게시물의 범위
            #    board_no.append(idx+1)

            # board_no 리스트의 길이를 활용하여 해결
            no = len(board_no) + 1

            # no = len(board_no)+1을 하면 숫자로 계산했기 때문에 input을 쓸 때 int로 바꿔줘야함.
            board_no.append(no)
            board_hit.append(0)  # 좋아요
            board_visitcount.append(0)  # 조회수

            print(f"{no}번의 게시글이 등록되었습니다.")

    elif select == '2':
        print("게시글 전체보기 탭에 진입하였습니다.")
        # 게시글 리스트 보기용 코드 추가 for

        print("=======================================")
        print("번호\t 제목\t 작성자\t 조회수\t ")
        print("=======================================")

        if len(board_no) == 0 :  # 게시물이 없을때
            print("등록된 게시물이 없습니다.")
            continue  #while문으로 돌아간다.

        for i in range(len(board_no)):  # 게시글의 개수만큼 반복(0~게시물수까지 인덱스 처리용)
            print(f"{board_no[i]}\t {board_title[i]}\t {board_writer[i]}\t {board_visitcount[i]}")
            #            번호,            제목,              작성자,                 조회수

    elif select == '3':
        print("게시글 자세히보기 탭에 진입하였습니다.")
        # 게시글 자세히 보기 코드 추가

        bno = int(input("게시글 번호 : "))

        if bno in board_no:   # 등록된 게시물의 유무 확인
            print("게시물을 찾았습니다.")
            idx = board_no.index(bno)  # 리스트에서 게시물의 인덱스 값을 찾아옴

            board_visitcount[idx] += 1  # 조회수 1 증가

            print("===========================================")
            print(f"번호 : {board_no[idx]}")
            print(f"제목 : {board_title[idx]}")
            print(f"내용 : {board_content[idx]}")
            print(f"작성자 : {board_writer[idx]}")
            print(f"조회수 : {board_visitcount[idx]}")
            print(f"좋아요 : {board_hit[idx]}")
            print("===========================================")

            if input("좋아요 누르기 (y) : ") == "y" :
                board_hit[idx] += 1
                print("좋아요 +1")
            else :
                print("아쉽습니다. 다음에 더 좋은 게시글이 되겠습니다.")
        else :
            print("해당 번호의 게시물을 찾지 못했습니다.")

    elif select == '4':
        print("게시글 수정하기 탭에 진입하였습니다.")
        # 게시글 수정 코드 추가

        bno = int(input("수정할 게시글 번호 : "))

        if bno in board_no:
            print("수정할 게시물을 찾았습니다.")
            idx = board_no.index(bno)
            print(f"제목 : {board_title[idx]}, 내용 : {board_content[idx]}, 작성자 : {board_writer[idx]}")

            print("수정할 항목을 선택하세요.")
            print("1. 제목")
            print("2. 내용")
            print("3. 작성자")
            print("4. 비밀번호")

            choice = input("선택 : ")

            if choice == "1":
                board_title[idx] = input("제목 수정 : ")
                print("제목이 수정되었습니다. " + board_title[idx])
            elif choice == "2":
                board_content[idx] = input("내용 수정 : ")
                print("내용이 수정되었습니다. " + board_content[idx])
            elif choice == "3":
                board_writer[idx] = input("작성자 수정 : ")
                print("작성자가 수정되었습니다. " + board_writer[idx])
            elif choice == "4":
                board_password[idx] = input("비밀번호 수정 : ")
                print("비밀번호가 수정되었습니다. " + board_password[idx])
            else :
                print("수정이 취소되었습니다.")
        else :
            print("수정할 항목이 입력되지 않았습니다.")
            print("처음으로 돌아갑니다.")

    elif select == '5':
        print("게시글 삭제하기 탭에 진입하였습니다.")
        # 게시글 삭제 코드 추가

        bno = int(input("삭제할 게시물 번호 : "))

        print("삭제할 게시물을 찾았습니다.")
        print(f"제목 : {board_title[bno]}, 내용 : {board_content[bno]}, 작성자 : {board_writer[bno]}")

        if bno in board_no:
            bnx = board_no.index(bno)
            print(f"{board_no[bnx]}번 게시글을 삭제합니다.")

            if input("정말 삭제할까요? (y) : ") == "y" :
                board_no.pop(bnx)
                board_title.pop(bnx)
                board_content.pop(bnx)
                board_writer.pop(bnx)
                board_password.pop(bnx)
                board_hit.pop(bnx)
                board_visitcount.pop(bnx)
                print("삭제가 완료되었습니다.")
            else :
                print("삭제가 취소되었습니다.")
        else :
            print("삭제할 번호가 없습니다.")
            print("처음으로 돌아갑니다.")

    elif select == '6':
        print("비회원 게시판 프로그램을 종료합니다.")
        run = False

    else :
        #1~6까지 잘못 입력된 값 처리용
        print("1~6번 중 원하시는 메뉴를 입력해주세요.")