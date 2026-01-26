# 상품에 대한 CRUD를 구현해보자
# c : 새상품 등록
# r : 전체상품 목록
# r : 단일상품 자세히보기
# u : 상품 수정하기
# d : 상품 품절(매진)

# 사용할 변수 (전역변수)
run = True

item_names = ["노트북","모니터"]  # 상품명
unit_prices = [1200000,400000]  #단가
quantity = [40,25]   # 수량
product_infor = ["AI용 삼성 노트북","LG 24인치 LED"]  # 상품 정보
category = ["가전","잡화"]  # 상품 분류
item_sns = [0,1]  # 상품 번호

# 사용할 메서드(함수)
def new_item():
    #print("new_item() 함수 호출 완료")   # 만들때 쓰고 실행할때 주석처리
    print("\n[새 상품 등록]")
    # 새상품 추가용 실행문

    name = input("상품명 : ")
    price = int(input("단가 : "))
    qut = int(input("수량 : "))
    pin = input("상품 정보 : ")
    ctg = input("상품 분류 : ")

    if input("저장하시겠습니까? y/n : ") == "y":

        item_names.append(name)
        unit_prices.append(price)
        quantity.append(qut)
        product_infor.append(pin)
        category.append(ctg)

        itsn = int(len(item_sns))  #0번부터 실행되기 때문에 +1안함

        item_sns.append(itsn)

        print(f"{name} 상품이 등록되었습니다.")
    else:
        print("잘못 입력하였습니다.")

def item_list():
    #print("item_list() 함수 호출 완료")
    print("\n[현재 판매중인 상품 리스트]")
    # 리스트 출력용 for item in item_names:
    print("="*30)
    print("번호 | 상품명 | 가격 | 재고 | 카테고리")
    print("=" * 30)

    for i in range(len(item_names)):
        print(f"{item_sns[i]} | {item_names[i]} | {unit_prices[i]} | {quantity[i]} | {category[i]}")

def item_view():
    #print("item_view() 함수 호출 완료")
    print("\n[상품 자세히 보기]")
    # 상품에 대한 상세 정보 표시
    item_list()

    sdx = int(input("상세 정보 확인할 상품 번호 : "))

    if 0<= sdx < len(item_sns):
        print("\n[제품 상세 정보]")
        print(f"상품명 : {item_names[sdx]}")
        print(f"가격 : {unit_prices[sdx]}")
        print(f"재고 : {quantity[sdx]}")
        print(f"상품 정보 : {product_infor[sdx]}")
        print(f"카테고리 : {category[sdx]}")
    else:
        print("존재하지 않는 상품입니다.")

def item_update():
    #print("item_update() 함수 호출 완료")
    print("\n[상품 수정 하기]")
    # 상품에 대한 정보 수정 하기
    item_list()

    sdx = int(input("\n수정하실 상품 번호 : "))

    if 0<= sdx < len(item_sns):
        #name = input(f"상품명{item_names[sdx]} : ")
        #price = input(f"가격{unit_prices[sdx]} : ")
        #qut = input(f"재고{quantity[sdx]} : ")
        #pin = input(f"상품 정보{product_infor[sdx]} : ")
        #ctg = input(f"카테고리{category[sdx]} : ")

        #name = input(상품명 : ")
        #price = int(input(가격 : "))
        #qut = int(input(재고 : "))
        #pin = input(상품 정보 : ")
        #ctg = input(카테고리 : ")  이렇게 하면 안돼나?

        print("\n1. 상품명 수정하기")
        print("2. 가격 수정하기")
        print("3. 재고 수정하기")
        print("4. 상품 정보 수정하기")
        print("5. 카테고리 수정하기")

        idx = input("수정할 항목 : ")

        if idx =="1":
            print("상품명 수정")
            item_names[sdx] = input("변경 상품명 : ")
            print(f"상품명이 {item_names[sdx]}(으)로 변경되었습니다.")
        elif idx == "2":
            unit_prices[sdx] = int(input("변경 가격 : "))
            print(f"가격이 {unit_prices[sdx]}(으)로 변경되었습니다.")
        elif idx == "3":
            quantity[sdx] = int(input("변경 재고 : "))
            print(f"재고가 {quantity[sdx]}(으)로 변경되었습니다.")
        elif idx == "4":
            product_infor[sdx] = input("변경 상품 정보 : ")
            print(f"상품 정보가 {product_infor[sdx]}(으)로 변경되었습니다.")
        elif idx == "5":
            category[sdx] = input("변경 카테고리 : ")
            print(f"카테고리가 {category[sdx]}(으)로 변경되었습니다.")
        else:
            print("수정할 상품을 잘못 입력하셨습니다.")
    else:
        print("존재하지 않는 상품입니다.")

def item_delete():
    #print("item_delete() 함수 호출 완료")
    print("[상품 삭제 하기]")
    # 상품 품절, 삭제하기
    item_list()

    sdx = int(input("품절인 상품 번호 : "))

    if 0<= sdx < len(item_sns):
        quantity[sdx] = 0
        print(f"{item_names[sdx]} 상품이 품절되었습니다.")
    else:
        print("존재하지 않는 상품입니다.")

def main_menu():
    # """일때 작성한 메뉴를 앞으로 빼주기
    print("""
=======================
MBC 아카데미 쇼핑몰 입니다.
=======================

1. 상품 등록
2. 상품 리스트
3. 상품 자세히 보기
4. 상품 수정
5. 상품 삭제

9. 프로그램 종료
    """)

def item_add_menu():
    print("""
====== 상품 추가용 메뉴 진입======
1. 교재
2. 잡화
3. 음식
4. 패션

9. 종료         
    """)

# 프로그램 주실행 코드 시작
while run:
    main_menu()  # 메인 메뉴 함수 호출하여 출력(위에 만든 함수 안에 print가 있어서 앞에 안씀)

    select = input("숫자 입력 : ")

    if select == "1":
        item_add_menu()  # 아이템 추가용 메뉴 함수
        new_item()  # 아이템 추가용 코드

    elif select == "2":
        item_list()

    elif select == "3":
        item_view()

    elif select == "4":
        item_update()

    elif select == "5":
        item_delete()

    elif select == "9":
        run = False

    else:
        print("잘못된 숫자를 입력하셨습니다.")
        print("다시 입력 하세요.")
