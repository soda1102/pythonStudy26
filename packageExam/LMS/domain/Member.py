# 회원

class Member:
    def __init__(self, uid, pw, name, number, role="user", active=True):  #초기값
        self.uid = uid  #아이디
        self.pw = pw  #비밀번호
        self.name = name  #이름
        self.number = number  #전화번호
        self.role = role  #권한
        self.active = active  #활성화여부

    def __str__(self):  #print처리용
        status = "활성" if self.active else "비활성"
        return f"{self.uid}|{self.name}|{self.number}|{self.role}|{status}"

    def to_line(self):
        return f"{self.uid}|{self.pw}|{self.name}|{self.number}|{self.role}|{self.active}"

    @staticmethod  #객체x, 문자열o -> session.py에 @classmethod 처리
    def from_line(line: str):
        uid, pw, name, number, role, active = line.strip().split("|")
        return Member(
            uid = uid,
            pw = pw,
            name = name,
            number = number,
            role = role,
            active = (active == "True"))

    def is_admin(self):  #지금 객체가 관리자냐
        return self.role == "admin"

    def is_manager(self):  #지금 객체가 매니저냐
        return self.role == "manager"