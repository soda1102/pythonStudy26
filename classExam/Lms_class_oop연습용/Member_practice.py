# Member.py는 각 회원의 자료를 담당함.
# 웹 프로그래밍에 백엔드에는 데이터베이스와 결합하는데
# MemberDTO, MemberVO라는 이름으로 사용됨.
# DTO = Data Transger Object, 데이터 전송 객체 라고 부름.
# VO = Value Object, 값 그 자체 라고 부름.

# 회원 각각의 자료를 리스트가 아닌 변수에 담아 제공하려 함

class Member:  # 클래스는 무조건 대문자로 시작!
    def __init__(self, uid, pw, name, role="user", active=True):
        self.id = uid  # id
        self.pw = pw  # pw
        self.name = name  # 이름
        self.role = role  # 권한
        self.active = active  # 활성화여부

    # 클래스와 파일명은 무조건 대문자!!!!
    # 사용법
    # member = Member() -> 객체를 생성하여 변수(member)에 연결 / Member - 클래스
    # 이름을 가져오고 싶을때 member.id
    # 암호를 가져오고 싶을때 member.pw

    # 파일 저장용 문자열 변환
    def to_line(self):
        return f"{self.id}|{self.pw}|{self.name}|{self.role}|{self.active}\n"

    # 사용법
    # member = Member()
    # member.to_line() -> kkw|1234|김기원|admin|True 엔터
    # 메모장에 객체 기록용

    # 파일에서 불러온 내용 객체처리
    @classmethod  # 객체(self)가 아니라 클래스 자체를 (cls)를 다루는 메서드라고 정의
    def from_line(cls, line):  # line : 메모장의 한줄 문자열
        uid, pw, name, role, active = line.strip().split("|")
        #           이 변수들에 넣어라 <- 한줄 문자열에 엔터를 지우고 | 로 잘라서
        return cls(uid, pw, name, role, active == "True")
        # 문자열을 싹 합쳐서 객체로 만들어라(class Member)

    # 비권장 사용법
    # m = Member(uid, pw, name, role, active) -> 권장하지 않음.(바로넣는 방법)
    #      self를 사용하는 방법(객체변수)
    # 권장 사용법
    # m = Member.from_line(line)
    #      cls를 사용하는 방법(클래스 변수)
    # 권장 이유 : 객체 생성 책임을 클래스가 담당

    # ** 암기 **
    # 면접시 물어보는 내용
    # 직렬화(Serialization) : 객체를 저장 가능한 형태로 바꾸는 것
    #       member.to_line()
    # 역직렬화(Deserialization) : 저장된 데이터를 객체로 만들 때 사용. (@classmethod)
    #          member.from_line(line)
