#상품

class Item:
    def __init__(self,no, name, price, quantity, active="True"):
        self.no = no  # 상품번호
        self.name = name  #상품이름
        self.price = price  #상품가격
        self.quantity = quantity  #상품내용
        self.active = active  #판매여부

    #파일 저장용 직렬화
    def to_line(self):
        return f"{self.no}|{self.name}|{self.price}|{self.quantity}|{self.active}"

    #파일 로드용 역직렬화
    @staticmethod
    def from_line(self, line):
        no, name, price, quantity, active = line.strip().split("|")
        return Item(int(no), name, price, quantity, active == "True")