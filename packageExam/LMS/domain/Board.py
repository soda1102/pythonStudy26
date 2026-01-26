class Board:
    def __init__(self, no, title, content, writer, visitcount=0, hit=0, active=True):
        self.no = no  #순번
        self.title = title  #제목
        self.content = content  #내용
        self.writer = writer  #작성자
        self.visitcount = visitcount  #조회수
        self.hit = hit  # 공감
        self.active = active  #삭제여부

    #파일저장용 직렬화
    def to_line(self):
        return f"{self.no}|{self.title}|{self.content}|{self.writer}|{self.visitcount}|{self.hit}|{self.active}"

    #파일 로드용 역직렬화
    @staticmethod
    def from_line(line):
        no, title, content, writer, visitcount, hit, active = line.strip().split("|")
        return Board(int(no), title, content, writer, int(visitcount), int(hit), active == "True")