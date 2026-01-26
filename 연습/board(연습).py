# c 게시글 등록
# r 게시글 전체보기 / 자세히 보기
# u 게시글 수정
# d 게시글 삭제
# + 게시글 찾기 응용해보기

run = True

# 사용할 변수
board_no = [] #게시글 번호
board_title = [] #게시글 제목
board_content = [] #게시글 내용
board_writer = [] #작성자
board_password = [] #게시글 암호
board_hit = [] #좋아요
board_visitcount = [] #조회수

# 사용할 메뉴
menu = """
======================
MBC 아카데미 비회원 게시판
======================

1. 게시글 등록
2. 게시글 전체보기
3. 게시글 자세히보기
4. 게시글 찾기
5. 게시글 수정하기
6. 게시글 삭제하기
7. 프로그램 종료

"""


while run:
    print(menu)

    select = input("1~7번 중 원하시는 메뉴를 입력해주세요. : ")

    if select == "1":
        print("게시글 등록 메뉴에 진입하였습니다.")

        title = input("제목 : ")
        content = input("내용 : ")
        writer = input("작성자 : ")
        password = input("암호 : ")

        print(f"제목 : {title}, 내용 : {content}")
        print(f"작성자 : {writer}")

        choose = input("저장하시겠습니까? (y / n) : ")

        if choose == "y":
            board_tittle.append(title)
            board_content.append(content)
            board_writer.append(writer)
            board_password.append(password)

            no = len(board_no) + 1
            board_no.append(no) #게시물 순번
            board_hit.append(0) # 좋아요
            board_visitcount.append(0) # 조회수

            print(f"{no}번의 게시글이 등록되었습니다.")

        else :
            print("저장되지 않았습니다.")
            print("처음으로 돌아갑니다.")

    elif select == "2":
        print("게시글 전체보기 메뉴에 진입하셨습니다.")

        print("--------------------------------")
        print("번호\t 제목\t 작성자\t 조회수\t")
        print("--------------------------------")

        if len(board_no) == 0:
            print("등록된 게시물이 없습니다.")
            continue

        for i in range(len(board_no)):
            print(f"{board_no[i], board_title[i], board_writer[i], board_visitcount[i]}")

    elif select == "3":
        print("게시글 자세히보기 메뉴에 진입하셨습니다.")

        bno = int(input("게시글 선택 : "))

        if bno in board_no:
            print("게시글을 찾았습니다.")

            idx = board_no.index(bno)
            board_visitcount[idx] += 1

            print("---------------------------------------------")
            print(f"번호 : {board_no[idx]}")
            print(f"제목 : {board_title[idx]}")
            print(f"내용 : {board_content[idx]}")
            print(f"작성자 : {board_writer[idx]}")
            print(f"조회수 : {board_visitcount[idx]}")
            print(f"좋아요 : {board_hit[idx]}")
            print("---------------------------------------------")

            if input("좋아요를 누르시겠습니까? (y/n) : ") == "y":
                board_hit[idx] += 1
                print("좋아요를 눌렀습니다.")
            else:
                print("다음엔 더 유익한 게시글이 되기를 바랍니다.")

        else :
            print("게시글이 없습니다.")
            print("처음으로 돌아갑니다.")

    elif select == "4":
        print("게시글 찾기 메뉴에 진입하셨습니다.")

        print("게시글 검색")
        print("1. 제목으로 검색")
        print("2. 작성자로 검색")

        choose = input("검색할 항목을 선택하세요 : ")
        found = False

        if choose == "1":
            keyword = input("검색할 제목 키워드 : ").lower()

            print("번호\t 제목\t 작성자\t 조회수\t")
            for i in range(len(board_no)):
                if keyword in board_title[i].lower():
                    print(f"{board_no[i]}\t{board_title[i]}\t{board_writer[i]}\t{board_visitcount[i]}")
                    found = True

        if choose == "2":
            keyword = input("작성자 검색 : ").lower()
            print("번호\t 제목\t 작성자\t 조회수\t")
            for i in range(len(board_no)):
                if keyword in board_writer[i].lower():
                    print(f"{board_no[i]}\t{board_title[i]}\t{board_writer}\t{board_content[i]}")
                    found = True
        else :
            print("잘못된 선택입니다.")

        if not found:
            print("검색 결과가 없습니다.")

    elif select == "5":
        print("게시글 수정 메뉴에 진입하셨습니다.")

        bno = int(input("수정할 게시글 번호 입력 : "))

        if bno in board_no:
            print("수정할 게시글을 찾았습니다.")
            idx = board_no.index(bno)
            print(f" 제목 : {board_title[idx]}, 내용 : {board_content[idx]}, 작성자 : {board_writer[idx]}")

            print("게시글 수정")
            print("1. 제목 수정")
            print("2. 내용 수정")
            print("3. 작성자 수정")
            print("4. 암호 수정")

            choice = input("수정할 항목을 선택하세요 : ")

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
                board_password[idx] = input("암호 수정 : ")
                print("암호가 수정되었습니다. " + board_password[idx])
            else :
                 print("수정이 취소되었습니다.")
        else :
             print("수정할 항목이 선택되지 않았습니다.")
             print("처음으로 돌아갑니다.")

    elif select == "6":
        print("게시글 삭제 메뉴에 진입하셨습니다.")

        bno = int(input("삭제할 게시글 번호 : "))

        print("삭제할 게시글을 찾았습니다.")
        print(f"제목 : {board_title[bno]}, 내용 : {board_content[bno]}, 작성자 : {board_writer[bno]}")

        if bno in board_no:
            bnx = board_no.index(bno)
            print(f"{board_no[bnx]}번의 게시글을 삭제합니다.")

            if input("정말 삭제하시겠습니까? (y/n) : ") == "y":
                board_no.pop[bnx]
                board_title.pop[bnx]
                board_content.pop[bnx]
                board_writer.pop[bnx]
                board_password.pop[bnx]
                board_hit.pop[bnx]
                board_visitcount.pop[bnx]
                print("삭제가 완료되었습니다.")
            else:
                print("삭제가 취소되었습니다.")
        else :
            print("삭제할 게시글의 번호가 없습니다.")
            print("처음으로 돌아갑니다.")

    elif select == "7":
        print("프로그램을 종료합니다.")
        run = False
else :
    print("잘못 입력하셨습니다.")
    print("1~7번 중 원하시는 메뉴를 입력해주세요.")