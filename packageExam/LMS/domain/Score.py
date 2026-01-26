#성적

class Score:
    def __init(self, uid, pyt, db, www):
        self.uid = uid
        self.pyt = pyt
        self.db = db
        self.www = www

    @property
    def total(self):  #변수 : s.total
        return self.pyt + self.db +self.www

    @property
    def avg(self):  #변수 : s.avg
        return round(self.total / 3, 2)

    @property
    def grade(self):  #변수 : s.grade
        if self.avg >= 90:
            return "A"
        elif self.avg >= 80:
            return "B"
        elif self.avg >= 70:
            return "C"
        else:
            return "F"

    def to_line(self):
        return f"{self.uid}|{self.pyt}|{self.db}|{self.www}\n"

    # @classmethod
    # def from_line(cls, line):
    #     uid, pyt, db, www = line.strip().split("|")
    #     return cls(uid, int(pyt), int(db), int(www))

    @staticmethod  # 객체x, 문자열o -> session.py에 @classmethod 처리
    def from_line(line: str):
        uid, pyt, db, www = line.strip().split("|")
        return Score(
            uid = uid,
            pyt = int(pyt),
            db = int(db),
            www = int(www))
    # 숫자만 입력하게 하고 싶을때 try_else 참고해서 main에 적용시키기