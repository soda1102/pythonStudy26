# 회원가입, 로그인, 로그아웃, 내정보수정(암호,전화번호,이름변경), 관리자페이지(암호,등급,블랙리스트여부), 프로그램종료

class Member:
    def __init__(self, uid, pw, name, number, role = "user", active = True):
        self.uid = uid  # 아이디
        self.pw = pw  # 암호
        self.name = name  # 이름
        self.number = number  # 전화번호
        self.role = role  # 등급
        self.active = active  # 활성화여부

    # member = Member(uid, pw, name, number)
    def __str__(self):
        status = "활성화" if self.active else "비활성화"
        return f"{self.uid}|{self.pw}|{self.name}|{self.number}|{self.role}|{status}"

    def to_line(self):
        return f"{self.uid}|{self.pw}|{self.name}|{self.number}|{self.role}|{self.active}"

    @staticmethod
    def from_line(line: str):
        uid,pw,name,number,role,active = line.strip().split("|")
        return Member(
            uid = uid,
            pw = pw,
            name = name,
            number = number,
            role = role,
            active = (active == "True"))

    # @classmethod
    def is_admin(self):
        return self.role == "admin"

    # @classmethod
    def is_manager(self):
        return self.role == "manager"