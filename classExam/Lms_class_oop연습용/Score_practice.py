class Score:
    def __init__(self, uid, pw, name, pyt="", db="", www="", tot="", avg="", grade="", role="user"):
        self.id = uid  # 학생 학번
        self.pw = pw  # 학생 비번
        self.name = name  # 학생 이름
        self.pyt = pyt  # 파이썬점수
        self.db = db  # 데이터베이스 점수
        self.www = www  # 웹 점수
        self.tot = tot  # 총점
        self.avg = avg  # 평균
        self.grade = grade  # 등급
        self.role = role  # 권한

    def to_line(self):
        return f"{self.id}|{self.pw}|{self.name}|{self.pyt}|{self.db}|{self.www}|{self.tot}|{self.avg}|{self.grade}|{self.role}\n"

    # 파일에서 불러온 내용 객체처리
    @classmethod
    def from_line(cls, line):
        uid, pw, name, pyt, db, www, tot, avg, grade, role = line.strip().split("|")
        return cls(uid, pw, name, pyt, db, www, tot, avg, grade, role)
