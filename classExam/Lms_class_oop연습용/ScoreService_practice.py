import os.path
from Score_practice import Score


class ScoreService:
    def __init__(self, file_name = "score.txt"):
        self.file_name = file_name
        self.scores = []
        self.session = None
        self.load_scores()

    def run(self):
        run = True
        while run:
            self.main_menu()
            sel = input(">>> ")

            if sel == "1": self.score_add()  # 회원가입
            elif sel == "2": self.score_login()  # 로그인
            elif sel == "3": self.score_check()  # 성적 확인
            elif sel == "9": run = False
            else:
                print("잘못 입력하셨습니다.")

    def load_scores(self):
        if not os.path.exists(self.file_name):
            self.save_scores()
            return

        self.scores = []
        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:
                self.scores.append(Score.from_line(line))

    def main_menu(self):
        print("""
======= 성적관리 프로그램 (Score 객체 기반) =======
1. 회원가입   2. 로그인   3. 내 성적 보기   9. 종료
               
        """)

    def score_login(self):
        if self.session is not None:
            print("이미 로그인한 사용자입니다.")
            return

        print("\n[로그인]")

        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        score = self.find_score(uid)

        if not score:
            print("존재하지 않는 아이디입니다.")
            return

        if score.pw == pw:
            self.session = score
            print(f"{score.name}님 로그인 성공")

            if score.role == "admin":
                self.scores_admin()
        else:
            print("비밀번호를 잘못 입력하셨습니다.")

    def score_check(self):
        if self.session is None:
            print(self.session)
            print("로그인 후 이용해주세요.")
            self.score_login()
            return

        print("\n[내 성적 보기]")

        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        score = self.find_score(uid)

        if score.pw == pw:
            self.session = score
            print(self.session)
            print(score)
            print(f"이름 : {score.name}")
            print(f"파이썬 : {self.scores.pyt}, 데이터베이스 : {self.scores.db}, 웹 : {self.scores.www}")
            print(f"평균 : {self.scores.avg}, 등급 : {self.scores.grade}")

    def save_scores(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for score in self.scores:
                f.write(score.to_line())

    def find_score(self, uid):
        for score in self.scores:
            if score.id == uid:
                print(score.name, "님을 찾았습니다.")
                return score
        return None

    def scores_admin(self):
        subrun = True
        while subrun:
            print("""
    ===== 교수 전용 메뉴 =====
    1. 성적 입력
    2. 성적 전체 보기
    3. 성적 수정
    4. 정보 삭제
    5. 종료        
            
            """)

            sel = input("선택 : ")
            if sel == "1":
                id = input("학생 아이디 : ")
                name = input("학생 이름 : ")
                pyt = int(input("파이썬 점수 :"))
                db = int(input("데이터베이스 점수 : "))
                www = int(input("웹 점수 : "))

                tot = pyt + db + www
                avg = tot / 3

                grade = self.getgrade(avg)

                print("입력한 정보를 확인하세요.")
                print(f"아이디 : {id}, 이름 : {name}")
                print(f"파이썬 : {pyt}, 데이터베이스 : {db}, 웹 : {www}")
                print(f"총점 : {tot}, 평균 : {avg}, 등급 : {grade}")

                if input("저장하시려면 y : ") == "y":
                    self.save_scores()
                    print(f"{name}님 성적 저장 완료")
                else:
                    print("성적 저장이 취소되었습니다.")
                    print("다시 시도해주세요.")


            elif sel == "2": #성적전체보기
                self.show_score_list()

            elif sel == "3": #성적수정

                uid = input("대상 아이디 : ")
                score = self.find_score(uid)

                if score:
                    print("\n[성적 수정할 과목]")
                    print("1. 파이썬")
                    print("2. 데이터베이스")
                    print("3. 웹")

                    choice = input("선택 : ")

                    if choice == "1":
                        score.pyt = int(input("수정할 파이썬 점수 : "))
                        print("파이썬 점수 수정 완료")
                    elif choice == "2":
                        score.db = int(input("수정할 데이터베이스 점수 : "))
                        print("데이터베이스 점수 수정 완료")
                    elif choice == "3":
                        score.www = int(input("수정할 웹 점수 : "))
                        print("웹 점수 수정 완료")

                    self.save_scores()

                else:
                    print("찾으시는 아이디가 존재하지 않습니다.")

            elif sel == "4": #정보삭제
                uid = input("대상 아이디 : ")
                score = self.find_score(uid)
                if score:
                    self.scores.remove(self.score)
                else:
                    print("찾는 아이디가 없습니다.")


    # def score_list(self):
    #     print("\n[내 성적 확인하기]")
    #
    #
    #     for score in self.scores:
    #         print(f"{score.id:10} {score.name:10} {score.pyt:10} {score.db:10} {score.www:10} {score.grade:10}")
    #     print("-"*60)

    def show_score_list(self):
        print("\n[성적 목록]")
        print("-" * 60)
        print(f"{'ID':10} {'이름':10} {'파이썬':10} {'데이터베이스':10} {'웹':10} {'등급':10}")
        print("-" * 60)

        for score in self.scores:
            print(f"{score.id:10} {score.name:10} {score.pyt:10} {score.db:10} {score.www:10} {score.grade:10}")
        print("-" * 60)

    def getgrade(self, avg):
        if avg > 90:
            return "A"
        elif avg > 80:
            return "B"
        elif avg > 70:
            return "C"
        else:
            return "F"

    def score_add(self):
        print("\n[회원가입]")

        uid = input("아이디 : ")

        if self.find_score(uid):  # 자주쓰는 중복코드로 메서드 처리함.
            print("이미 존재하는 아이디입니다.")
            return

        pw = input("비밀번호 : ")
        name = input("이름 : ")
        pyt = ""
        db = ""
        www = ""
        tot = ""
        avg = ""
        grade = ""
        role = "user"


        if input("회원가입을 하시겠습니까? y : ") == "y":
            self.scores.append(Score(uid, pw, name, pyt, db, www, tot, avg, grade, role))
            self.save_scores()  # 파일로 기록
            self.load_scores()  # 파일에서 다시 불러와
            print("회원가입 완료")

