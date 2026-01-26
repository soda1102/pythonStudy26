# 파이썬에 oop를 적용해보자
# oop : 객체 지향 프로그래밍, Object-Oriented Programming
# 는 현실 시계의 '객체' 개념을 기반으로 데이터를 속성(데이터)과
# 행위(메서드)로 묶어 관리하고.
# 객체 간 상호작용을 통해 프로그램을 설계하는 프로그래밍 패러다임으로
# 코드 재사용, 유지보수 용이성, 가독성 향상 등의 장점이 있으며,
# 캡슐화, 상속, 다형성 등의 핵심 원칙을 가집니다.

# 지금까지는 2차원 배열을 이용해서 인덱스로 데이터에 접근을 함.
# [0] 이곳에 무엇이 들어있는지 암기를 하고 [4]에는 무엇이 들어갈지?
# 메모장에 한줄로 되어있는 자료를 클래스로 만들면
# Member.name / Member.id / Member.pw 등으로 접근할 수 있다.

# Member.py는 개인의 객체 -> 변수와 게터(나오는 값 처리)/세터(입력값 처리) 등을 담당함.
# 게터 : 값을 가져오는 것(변조해야하는 것들) / 세터 : 입력 값을 검증해야 하는 것
# MemberService.py는 CRUD용 메서드들이 들어있는 모듈
# main.py는 주 실행 코드

from MemberService import MemberService
#                            클래스 연결
# 외부 파일(모듈) 가져오라는 뜻
from classExam.Lms_class_oop연습용.ScoreService_practice import ScoreService


app = MemberService()  # 회원서비스 클래스를 app이라는 변수에 연결
# app.run()  # app 변수에 연결된 클래스 안에 run() 메서드 실행

app1 = ScoreService()
# app1.run()

run = True

while run:
    print("원하시는 메뉴를 선택해주세요.")
    print("1. 회원관리")
    print("2. 성적관리")

    select = input(">>> ")

    if select == "1":
        app.run()
    elif select == "2":
        app1.run()