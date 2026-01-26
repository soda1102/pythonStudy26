# 커피 자판기 상품 페이지 만들기

# while문 : run, subRun
# if문 : 메뉴선택이나 판단용
# for문 : 리스트에 있는 전체내용 출력용
# for in : 리스트에 있는 내용 인덱스 찾는 용
# c: 상품등록(판매자만) / r: 상품리스트, 상품자세히보기 / u: 상품 수정 / d: 상품 품절 및 삭제

# 자판기 판매 메뉴 : 커피, 라떼, 코코아, 우유, 아이스티, 빵 등

# 필요한 변수

run = True
session = None   #로그인한 사용자

# 자판기 메뉴에 대한 리스트
coffee_no = [1,2,3,4,5]   #커피 번호
beverage_no = [1,2,3,4,5,6]   #음료 번호
dessert_no = [1,2,3]    #디저트 번호
coffee_title = ["아메리카노(아이스)","아메리카노(핫)","카페라떼(아이스)","카페라떼(핫)","콜드브루(아이스)"]
beverage_title = ["딸기라떼","복숭아 아이스티","레몬 아이스티","레몬에이드","캐모마일(아이스)","캐모마일(핫)"]
dessert_title = ["딸기케이크","마카롱","샌드위치"]
coffee_name = ["americano_ice","americano_hot","latte_ice","latte_hot","coldbrew"]   #커피 이름
beverage_name = ["strawberry_latte","peach_icedtea","lemon_icedtea","lemon_ade","camomile_ice","camomile_hot"]   #음료 이름
dessert_name = ["strawberry_cake","macaroon","sandwich"]    #디저트 이름
coffee_price = [1900,1900,2100,2100,2500]   #커피 가격
beverage_price = [3200,2800,2800,3000,2300,2300]   #음료 가격
dessert_price = [4200,2800,4500]    #디저트 가격

#
money = []   #돈

#홈페이지 로그인
sns = [1,2,3]   #회원번호
ids = ["admin","manager","staff"]   #아이디
names = ["관리자","매니저","직원"]
groups = ["admin","manager","staff"]   #회원등급
pws = ["1234","5678","3456"]   #관리자 비밀번호
numbers = ["01012341234","01023452345","01056785678"]


mainMenu = """
==========================
MBC 카페에 오신것을 환영합니다.
==========================

1. MBC카페 소개
2. 메뉴 소개
3. 메뉴 자세히보기 및 구매하기
4. 메뉴 등록하기(관리자만)
5. 메뉴 수정 (관리자만)
6. 회원가입 및 로그인
7. 프로그램 종료

"""

subMenu1 = """
=======================
MBC 카페 소개 페이지입니다.
=======================

1. 브랜드 소개
2. 비전체계
3. 메인 페이지로 돌아가기

"""

subMenu2 = """
============================
MBC 카페 메뉴 소개 페이지입니다.
============================

1. 커피
2. 커피 외 음료
3. 디저트
4. 메인 페이지로 돌아가기

"""

subMenu3 = """
==================================
MBC 카페 메뉴 자세히 보기 페이지입니다.
==================================

1. 커피 메뉴 자세히 보기
2. 커피 외 음료 자세히 보기
3. 디저트 자세히 보기
4. 메인 페이지로 돌아가기

"""

subMenu4 = """
==================================
MBC 카페 상품 등록하기 페이지입니다.
==================================

1. 커피 메뉴 등록하기
2. 커피 외 음료 등록하기
3. 디저트 등록하기
4. 메인페이지로 돌아가기

"""

subMenu5 = """
==================================
MBC 카페 상품 수정하기 페이지입니다.
==================================

1. 커피 메뉴 수정하기
2. 커피 외 음료 수정하기
3. 디저트 수정하기
4. 메인페이지로 돌아가기

"""


subMenu6 = """
===================================
MBC 카페 회원가입 및 로그인 페이지입니다.
===================================

1. 로그인
2. 회원가입
3. 회원수정
4. 권한설정
5. 메인페이지로 돌아가기

"""


while run:
    print(mainMenu)   #메인메뉴 출력
    select = input("보기 원하시는 번호를 입력해주세요 : ")

    if select == "1":
        print("\nMBC 카페 소개 페이지로 진입합니다.")

        subRun = True

        while subRun:
            print(subMenu1)

            select = input("원하시는 번호를 입력해주세요 : ")

            if select == "1":   #카페 브랜드 소개
                print("\nMBC 카페 브랜드 소개페이지 입니다.")

                print("""
                ====================[MBC카페] ====================
                 저희 MBC 카페는 10년 이상의 경력이 있는 바리스타와 함께
                  언제 어디서나 부담스럽지 않은 가격으로 모든 사람들에게
                   사랑받을 수 있도록 질 좋은 커피를 제공하고 있습니다.
                """)


            elif select == "2":   #카페 비전체계
                print("\nMBC 카페 비전 체계 소개페이지 입니다.")

                print("""
                ==================[MBC카페]===================
                저희 MBC 카페는 세계에서 가장 많이 사랑받는 브랜드가
                    되고자 하는 목표를 가지고 나아가고 있습니다.
                앞으로 더 많은 고객에게 좋은 커피를 제공할 수 있도록
                 커피 문화의 지속적인 가치를 창조하며 더욱 차별화된
                        제품과 서비스를 선보일 것입니다. 
                
                """)

            elif select == "3":   #처음으로 돌아가기
                subRun = False

            else :
                print("\n보기 원하시는 번호를 정확히 입력해주세요.")

    elif select == "2":
        print("\nMBC 카페 메뉴 소개 페이지입니다.")

        subRun = True

        while subRun:
            print(subMenu2)

            select = input("원하시는 번호를 입력해주세요 : ")

            if select == "1":   #커피 메뉴 전체보기
                print("\n커피 전체 보기 페이지입니다.")

                print("-------------------")
                print("번호\t커피이름\t")
                print("-------------------")

                if len(coffee_no) == 0:
                    print("등록된 정보가 없습니다.")
                    continue
                for i in range(len(coffee_no)):
                    print(f"{coffee_no[i]}\t{coffee_title[i]}\t")


            elif select == "2":  #커피 외 음료 전체 보기
                print("\n커피 외 음료 전체보기 페이지입니다.")

                print("----------------------")
                print("번호\t음료이름\t")
                print("----------------------")

                if len(beverage_no) == 0:
                    print("등록된 정보가 없습니다.")
                    continue
                for i in range(len(beverage_no)):
                    print(f"{beverage_no[i]}\t{beverage_title[i]}\t")

            elif select == "3":   #디저트 전체보기
                print("\n디저트 전체보기 페이지입니다.")

                print("-------------------------")
                print("번호\t디저트이름\t")
                print("-------------------------")

                if len(dessert_no) == 0:
                    print("등록된 정보가 없습니다.")
                    continue
                for i in range(len(dessert_no)):
                    print(f"{dessert_no[i]}\t{dessert_title[i]}\t")

            elif select == "4":   #처음으로 돌아가기
                subRun = False

            else:
                print("잘못된 번호를 입력하셨습니다.")

    elif select == "3":   #메뉴자세히보기
        print("\nMBC 카페 메뉴 자세히 보기 페이지입니다.")

        subRun = True

        while subRun:
            print(subMenu3)

            select = input("원하시는 번호를 입력해주세요 : ")

            if select == "1": #커피 메뉴 자세히보기 및 구매하기
                print("[커피 메뉴 자세히 보기]")

                print("1. 아메리카노(ICE)")
                print("2. 아메리카노(HOT)")
                print("3. 카페라떼(ICE)")
                print("4. 카페라떼(HOT)")
                print("5. 콜드브루(ONLY ICE)")
                print("6. 뒤로가기")

                subChoice = int(input("커피메뉴 번호 : "))
                cdx = coffee_no.index(subChoice)

                if subChoice == "1":   #아이스아메리카노

                    print("---------------------------------")
                    print(f"상품번호 : {coffee_no[cdx]}")
                    print(f"상품이름 : {coffee_title[cdx]}")
                    print(f"상품가격 : {coffee_price[cdx]}원")
                    print("---------------------------------")

                    print("아메리카노(ICE)를 구매하시겠습니까?")

                    if input("구매하시려면 y : ") == "y":

                        americano_ice = 10
                        while True:
                            money = int(input("돈을 넣어주세요 : "))
                            if money == 1900:
                                print("결제가 완료되었습니다.")
                                americano_ice = americano_ice - 1
                                print("남은 아메리카노(ICE)는 %d개 입니다." % americano_ice)
                                break
                            elif money > 1900:
                                print("거스름돈 %d원을 드리겠습니다." % (money - 1900))
                                americano_ice = americano_ice - 1
                            else:
                                print("금액이 부족합니다.")
                                print("남은 아메리카노(ICE)는 %d개 입니다." % americano_ice)
                            if americano_ice == 0:
                                print("모든 커피가 소진되었습니다. 판매를 중지합니다.")
                                break
                    else:
                        print("잘못 입력 하셨습니다.")

                elif subChoice == "2":   #핫아메리카노

                    print("---------------------------------")
                    print(f"상품번호 : {coffee_no[cdx]}")
                    print(f"상품이름 : {coffee_title[cdx]}")
                    print(f"상품가격 : {coffee_price[cdx]}원")
                    print("---------------------------------")

                    print("아메리카노(HOT)를 구매하시겠습니까?")

                    if input("구매하시려면 y : ") == "y":

                        americano_hot = 10
                        while True:
                            money = int(input("돈을 넣어주세요 : "))
                            if money == 1900:
                                print("결제가 완료되었습니다.")
                                americano_hot = americano_hot - 1
                                print("남은 아메리카노(HOT)는 %d개 입니다." % americano_hot)
                                break
                            elif money > 1900:
                                print("거스름돈 %d원을 드리겠습니다." % (money - 1900))
                                americano_hot = americano_hot - 1
                            else:
                                print("금액이 부족합니다.")
                                print("남은 아메리카노(HOT)는 %d개 입니다." % americano_hot)
                            if americano_hot == 0:
                                print("모든 커피가 소진되었습니다. 판매를 중지합니다.")
                                break
                    else:
                        print("잘못 입력 하셨습니다.")

                elif subChoice == "3":   #아이스카페라떼

                    print("---------------------------------")
                    print(f"상품번호 : {coffee_no[cdx]}")
                    print(f"상품이름 : {coffee_title[cdx]}")
                    print(f"상품가격 : {coffee_price[cdx]}원")
                    print("---------------------------------")

                    print("카페라떼(ICE)를 구매하시겠습니까?")

                    if input("구매하시려면 y : ") == "y":

                        latte_ice = 10
                        while True:
                            money = int(input("돈을 넣어주세요 : "))
                            if money == 2100:
                                print("결제가 완료되었습니다.")
                                latte_ice = latte_ice - 1
                                print("남은 카페라떼(HOT)는 %d개 입니다." % latte_ice)
                                break
                            elif money > 2100:
                                print("거스름돈 %d원을 드리겠습니다." % (money - 2100))
                                latte_ice = latte_ice - 1
                            else:
                                print("금액이 부족합니다.")
                                print("남은 카페라떼(HOT)는 %d개 입니다." % latte_ice)
                            if latte_ice == 0:
                                print("모든 커피가 소진되었습니다. 판매를 중지합니다.")
                                break
                    else:
                        print("잘못 입력 하셨습니다.")


                elif subChoice == "4":    #핫카페라떼

                    print("---------------------------------")
                    print(f"상품번호 : {coffee_no[cdx]}")
                    print(f"상품이름 : {coffee_title[cdx]}")
                    print(f"상품가격 : {coffee_price[cdx]}원")
                    print("---------------------------------")

                    print("카페라떼(HOT)를 구매하시겠습니까?")

                    if input("구매하시려면 y : ") == "y":

                        latte_hot = 10
                        while True:
                            money = int(input("돈을 넣어주세요 : "))
                            if money == 2100:
                                print("결제가 완료되었습니다.")
                                latte_hot = latte_hot - 1
                                print("남은 카페라떼(HOT)는 %d개 입니다." % latte_hot)
                                break
                            elif money > 2100:
                                print("거스름돈 %d원을 드리겠습니다." % (money - 2100))
                                latte_hot = latte_hot - 1
                            else:
                                print("금액이 부족합니다.")
                                print("남은 카페라떼(HOT)는 %d개 입니다." % latte_hot)
                            if latte_hot == 0:
                                print("모든 커피가 소진되었습니다. 판매를 중지합니다.")
                                break
                    else:
                        print("잘못 입력 하셨습니다.")


                elif subChoice == "5":   #콜드브루

                    print("---------------------------------")
                    print(f"상품번호 : {coffee_no[cdx]}")
                    print(f"상품이름 : {coffee_title[cdx]}")
                    print(f"상품가격 : {coffee_price[cdx]}원")
                    print("---------------------------------")

                    print("콜드브루(ONLY ICE)를 구매하시겠습니까?")

                    if input("구매하시려면 y : ") == "y":

                        coldbrew = 10
                        while True:
                            money = int(input("돈을 넣어주세요 : "))
                            if money == 2500:
                                print("결제가 완료되었습니다.")
                                coldbrew = coldbrew - 1
                                print("남은 콜드브루(ONLY ICE)는 %d개 입니다." % coldbrew)
                                break
                            elif money > 2500:
                                print("거스름돈 %d원을 드리겠습니다." % (money - 2500))
                                coldbrew = coldbrew - 1
                            else:
                                print("금액이 부족합니다.")
                                print("남은 콜드브루(ONLY ICE)는 %d개 입니다." % coldbrew)
                            if coldbrew == 0:
                                print("모든 커피가 소진되었습니다. 판매를 중지합니다.")
                                break
                    else:
                        print("잘못 입력 하셨습니다.")

                elif subChoice == "6":
                    subRun = False

                else:
                    print("원하시는 상품의 번호를 정확히 입력해주세요.")

            elif select == "2":   #커피 외 음료 자세히 보기 및 구매하기
                print("\n[커피 외 음료 메뉴 자세히 보기]")

                print("1. 딸기라떼")
                print("2. 복숭아 아이스티")
                print("3. 레몬아이스티")
                print("4. 레몬에이드")
                print("5. 캐모마일(ICE)")
                print("6. 캐모마일(HOT)")
                print("7. 뒤로가기")

                bno = int(input("음료메뉴 번호 : "))
                bnx = beverage_no.index(bno)

                if bno == "1":   #딸기라떼


                    print("---------------------------------")
                    print(f"상품번호 : {beverage_no[bnx]}")
                    print(f"상품이름 : {beverage_title[bnx]}")
                    print(f"상품가격 : {beverage_price[bnx]}원")
                    print("---------------------------------")

                    print("딸기라떼를 구매하시겠습니까?")

                    if input("구매하시려면 y : ") == "y":

                        strawberry_latte = 10
                        while True:
                            money = int(input("돈을 넣어주세요 : "))
                            if money == 3200:
                                print("결제가 완료되었습니다.")
                                strawberry_latte = strawberry_latte - 1
                                print("남은 딸기라떼는 %d개 입니다." % strawberry_latte)
                                break
                            elif money > 3200:
                                print("거스름돈은 %d원을 드리겠습니다." % (money - 3200))
                                strawberry_latte = strawberry_latte - 1
                            else:
                                print("금액이 부족합니다.")
                                print("남은 딸기라떼는 %d개 입니다." % strawberry_latte)
                            if strawberry_latte == 0:
                                print("모든 음료가 소진되었습니다. 판매를 중지합니다.")
                                break
                    else:
                        print("잘못 입력 하셨습니다.")

                elif bno == "2":   #복숭아 아이스티

                      print("---------------------------------")
                      print(f"상품번호 : {beverage_no[bnx]}")
                      print(f"상품이름 : {beverage_title[bnx]}")
                      print(f"상품가격 : {beverage_price[bnx]}원")
                      print("---------------------------------")

                      print("복숭아 아이스티를 구매하시겠습니까?")

                      if input("구매하시려면 y : ") == "y":

                          peach_icedtea = 10
                          while True:
                              money = int(input("돈을 넣어주세요 : "))
                              if money == 2800:
                                  print("결제가 완료되었습니다.")
                                  peach_icedtea = peach_icedtea - 1
                                  print("남은 복숭아 아이스티는 %d개 입니다." % peach_icedtea)
                                  break
                              elif money > 2800:
                                  print("거스름돈은 %d원을 드리겠습니다." % (money - 2800))
                                  peach_icedtea = peach_icedtea - 1
                              else:
                                  print("금액이 부족합니다.")
                                  print("남은 복숭아 아이스티는 %d개 입니다." % peach_icedtea)
                              if peach_icedtea == 0:
                                  print("모든 음료가 소진되었습니다. 판매를 중지합니다.")
                                  break
                      else:
                          print("잘못 입력 하셨습니다.")

                elif bno == "3":   #레몬 아이스티

                     print("---------------------------------")
                     print(f"상품번호 : {beverage_no[bnx]}")
                     print(f"상품이름 : {beverage_title[bnx]}")
                     print(f"상품가격 : {beverage_price[bnx]}원")
                     print("---------------------------------")

                     print("레몬 아이스티를 구매하시겠습니까?")

                     if input("구매하시려면 y : ") == "y":

                         lemon_icedtea = 10
                         while True:
                             money = int(input("돈을 넣어주세요 : "))
                             if money == 2800:
                                 print("결제가 완료되었습니다.")
                                 lemon_icedtea = lemon_icedtea - 1
                                 print("남은 레몬 아이스티는 %d개 입니다." % lemon_icedtea)
                                 break
                             elif money > 2800:
                                 print("거스름돈은 %d원을 드리겠습니다." % (money - 2800))
                                 lemon_icedtea = lemon_icedtea - 1
                             else:
                                 print("금액이 부족합니다.")
                                 print("남은 레몬 아이스티는 %d개 입니다." % lemon_icedtea)
                             if lemon_icedtea == 0:
                                 print("모든 음료가 소진되었습니다. 판매를 중지합니다.")
                                 break
                     else:
                         print("잘못 입력 하셨습니다.")

                elif bno == "4":   #레몬에이드

                     print("---------------------------------")
                     print(f"상품번호 : {beverage_no[bnx]}")
                     print(f"상품이름 : {beverage_title[bnx]}")
                     print(f"상품가격 : {beverage_price[bnx]}원")
                     print("---------------------------------")

                     print("레몬 에이드를 구매하시겠습니까?")

                     if input("구매하시려면 y : ") == "y":

                         lemonade = 10
                         while True:
                             money = int(input("돈을 넣어주세요 : "))
                             if money == 3000:
                                 print("결제가 완료되었습니다.")
                                 lemonade = lemonade - 1
                                 print("남은 레몬 에이드는 %d개 입니다." % lemonade)
                                 break
                             elif money > 3000:
                                 print("거스름돈은 %d원을 드리겠습니다." % (money - 3000))
                                 lemonade = lemonade - 1
                             else:
                                 print("금액이 부족합니다.")
                                 print("남은 레몬 에이드는 %d개 입니다." % lemonade)
                             if lemonade == 0:
                                 print("모든 음료가 소진되었습니다. 판매를 중지합니다.")
                                 break
                     else:
                         print("잘못 입력 하셨습니다.")

                elif bno == "5":  # 아이스 캐모마일

                    print("---------------------------------")
                    print(f"상품번호 : {beverage_no[bnx]}")
                    print(f"상품이름 : {beverage_title[bnx]}")
                    print(f"상품가격 : {beverage_price[bnx]}원")
                    print("---------------------------------")

                    print("캐모마일(ICE)을 구매하시겠습니까?")

                    if input("구매하시려면 y : ") == "y":

                        camomile_ice = 10
                        while True:
                            money = int(input("돈을 넣어주세요 : "))
                            if money == 2300:
                                print("결제가 완료되었습니다.")
                                camomile_ice = camomile_ice - 1
                                print("남은 캐모마일(ICE)은 %d개 입니다." % camomile_ice)
                                break
                            elif money > 2300:
                                print("거스름돈은 %d원을 드리겠습니다." % (money - 2300))
                                camomile_ice = camomile_ice - 1
                            else:
                                print("금액이 부족합니다.")
                                print("남은 캐모마일(ICE)은 %d개 입니다." % camomile_ice)
                            if camomile_ice == 0:
                                print("모든 음료가 소진되었습니다. 판매를 중지합니다.")
                                break
                    else:
                        print("잘못 입력 하셨습니다.")

                elif bno == "6":  # 핫 캐모마일

                    print("---------------------------------")
                    print(f"상품번호 : {beverage_no[bnx]}")
                    print(f"상품이름 : {beverage_title[bnx]}")
                    print(f"상품가격 : {beverage_price[bnx]}원")
                    print("---------------------------------")

                    print("캐모마일(HOT)을 구매하시겠습니까?")

                    if input("구매하시려면 y : ") == "y":

                        camomile_hot = 10
                        while True:
                            money = int(input("돈을 넣어주세요 : "))
                            if money == 2300:
                                print("결제가 완료되었습니다.")
                                camomile_hot = camomile_hot - 1
                                print("남은 캐모마일(HOT)은 %d개 입니다." % camomile_hot)
                                break
                            elif money > 2300:
                                print("거스름돈은 %d원을 드리겠습니다." % (money - 2300))
                                camomile_hot = camomile_hot - 1
                            else:
                                print("금액이 부족합니다.")
                                print("남은 캐모마일(HOT)은 %d개 입니다." % camomile_hot)
                            if camomile_hot == 0:
                                print("모든 음료가 소진되었습니다. 판매를 중지합니다.")
                                break
                    else:
                        print("잘못 입력 하셨습니다.")

                elif bno == "7":   #뒤로가기
                    subRun = False

                else:
                    print("원하시는 상품의 번호를 정확히 입력해주세요.")

            elif select == "3":   #디저트 자세히보기 및 구매하기
                print("\n[디저트 메뉴 자세히 보기]")

                print("1. 딸기케이크")
                print("2. 마카롱")
                print("3. 샌드위치")
                print("4. 뒤로가기")

                dno = int(input("디저트메뉴 번호 : "))
                ddx = dessert_no.index(dno)

                if dno == "1":

                    print("---------------------------------")
                    print(f"상품번호 : {dessert_no[ddx]}")
                    print(f"상품이름 : {dessert_title[ddx]}")
                    print(f"상품가격 : {dessert_price[ddx]}원")
                    print("---------------------------------")

                    print("딸기케이크를 구매하시겠습니까?")

                    if input("구매하시려면 y : ") == "y":

                        strawberry_cake = 3
                        while True:
                            money = int(input("돈을 넣어주세요 : "))
                            if money == 4200:
                                print("결제가 완료되었습니다.")
                                strawberry_cake = strawberry_cake - 1
                                print("남은 딸기케이크는 %d개 입니다." % strawberry_cake)
                                break
                            elif money > 4200:
                                print("거스름돈 %d원을 드리겠습니다." % (money - 4200))
                                strawberry_cake = strawberry_cake - 1
                            else:
                                print("금액이 부족합니다.")
                                print("남은 딸기케이크는 %d개 입니다." % strawberry_cake)
                            if strawberry_cake == 0:
                                print("모든 딸기케이크가 소진되었습니다. 판매를 종료합니다.")
                                break
                    else:
                        print("잘못 입력 하셨습니다.")

                elif dno == "2":   #마카롱

                    print("---------------------------------")
                    print(f"상품번호 : {dessert_no[ddx]}")
                    print(f"상품이름 : {dessert_title[ddx]}")
                    print(f"상품가격 : {dessert_price[ddx]}원")
                    print("---------------------------------")

                    print("마카롱을 구매하시겠습니까?")

                    if input("구매하시려면 y : ") == "y":

                        macaroon = 5
                        while True:
                            money = int(input("돈을 넣어주세요 : "))
                            if money == 2800 :
                                print("결제가 완료되었습니다.")
                                macaroon = macaroon - 1
                                print("남은 마카롱은 %d개 입니다." % macaroon)
                                break
                            elif money > 2800:
                                print("거스름돈 %d원을 드리겠습니다." % (money - 2800))
                                macaroon = macaroon - 1
                            else:
                                print("금액이 부족합니다.")
                                print("남은 마카롱은 %d개 입니다." % macaroon)
                            if macaroon == 0:
                                print("모든 마카롱이 소진되었습니다. 판매를 중지합니다.")
                                break
                    else:
                        print("잘못 입력하셨습니다.")

                elif dno == "3":   #샌드위치

                    print("---------------------------------")
                    print(f"상품번호 : {dessert_no[ddx]}")
                    print(f"상품이름 : {dessert_title[ddx]}")
                    print(f"상품가격 : {dessert_price[ddx]}원")
                    print("---------------------------------")

                    print("샌드위치를 구매하시겠습니까?")

                    if input("구매하시려면 y : ") == "y":

                        sandwich = 4
                        while True:
                            money = int(input("돈을 넣어주세요 : "))
                            if money == 4500:
                                print("결제가 완료되었습니다.")
                                sandwich = sandwich - 1
                                print("남은 샌드위치는 %d개 입니다." % sandwich)
                                break
                            elif money > 4500:
                                print("거스름돈 %d원을 드리겠습니다." % (money - 4500))
                                sandwich = sandwich - 1
                            else:
                                print("금액이 부족합니다.")
                                print("남은 샌드위치는 %d개 입니다." % sandwich)
                            if sandwich == 0:
                                print("모든 마카롱이 소진되었습니다. 판매를 중지합니다.")
                                break
                    else:
                        print("잘못 입력하셨습니다.")

            elif select == "4":   #처음으로 돌아가기
                subRun = False
            else:
                print("원하시는 상품의 번호를 정확히 입력해주세요.")

    elif select == "4":    #카페 상품 등록(관리자용)
        if session is None:
            print("관리자 전용 페이지 입니다. 로그인 후 이용해주세요!")
            continue

        else:
            print("\nMBC 카페 상품 등록하기 페이지입니다.")

            subRun = True

            while subRun:
                if groups[session] == "admin":
                    print(subMenu4)

                select = input("원하시는 번호를 입력해주세요 : ")

                if select == "1":   #커피 메뉴 등록

                    print("\n[MBC 카페 커피 상품 등록하기]")

                    cn = input("커피 이름(영문) : ")
                    ct = input("커피 이름(한글) : ")
                    cp = int(input("커피 금액 : "))

                    print(f"커피 이름(영문) : {cn}, 커피 이름(한글) : {ct}, 커피 금액 : {cp}원")

                    choice = input("저장하시려면 y를 입력해주세요 : ")

                    if choice == "y":
                        coffee_name.append(cn)
                        coffee_title.append(ct)
                        coffee_price.append(cp)

                        cpn = len(coffee_no) + 1

                        coffee_no.append(cpn)

                        print(f"{ct} 메뉴가 등록되었습니다.")
                    else:
                        print("잘못입력하셨습니다.")

                elif select == "2":   #음료 상품 등록하기
                    print("\n[MBC 카페 커피 외 음료 상품 등록하기]")

                    bn = input("음료 이름(영문) : ")
                    bt = input("음료 이름(한글) : ")
                    bp = int(input("음료 금액 : " + "원"))

                    print(f"음료 이름(영문) : {bn}, 음료 이름(한글) : {bt}, 음료 금액 : {bp}원")

                    choice = input("저장하시려면 y를 입력해주세요 : ")

                    if choice == "y":
                        beverage_name.append(bn)
                        beverage_title.append(bt)
                        beverage_price.append(bp)

                        bpn = len(beverage_no) + 1

                        beverage_no.append(bpn)

                        print(f"{bt} 메뉴가 등록되었습니다.")
                    else:
                        print("잘못입력하셨습니다.")

                elif select == "3":   #디저트 상품 등록하기
                    print("\n[MBC 카페 디저트 상품 등록하기]")

                    dn = input("디저트 이름(영문) : ")
                    dt = input("디저트 이름(한글) : ")
                    dp = int(input("디저트 금액 : "))

                    print(f"디저트 이름(영문) : {dn}, 디저트 이름(한글) : {dt}, 음료 금액 : {dp}원")

                    choice = input("저장하시려면 y를 입력해주세요 : ")

                    if choice == "y":
                        dessert_name.append(dn)
                        dessert_title.append(dt)
                        dessert_price.append(dp)

                        dpn = len(dessert_no) + 1

                        dessert_no.append(dpn)

                        print(f"{dt} 메뉴가 등록되었습니다.")
                    else:
                        print("잘못입력하셨습니다.")

                elif select == "4":  # 처음으로 돌아가기
                    subRun = False

                else:
                    print("원하시는 번호를 정확히 입력해주세요.")


    elif select == "5":
        if session is None:
            print("관리자 전용 페이지 입니다. 로그인 후 이용해주세요!")
            continue

        if groups[session] == "admin":
            print("\nMBC 카페 상품 수정하기 페이지입니다.")

        subRun = True

        while subRun:
            print(subMenu5)

            select = input("원하시는 번호를 입력해주세요 : ")

            if select == "1":   #커피메뉴 수정하기
                print("\n[MBC 카페 커피 상품 수정하기]")

                c_no = int(input("상품 번호 : "))

                if c_no in coffee_no:
                    cdx = coffee_no.index(c_no)

                    coffee_name[cdx] = input("변경할 이름(영문) : ")
                    coffee_title[cdx] = input("변경할 이름(한글) : ")
                    coffee_price[cdx] = int(input("변경할 금액 : "))

                    print("상품이 수정되었습니다.")
                else:
                    print("상품 번호가 존재하지 않습니다.")

            elif select == "2":
                print("\n[MBC 카페 음료 상품 수정하기]")

                b_no = int(input("상품 번호 : "))

                if b_no in beverage_no:
                    bdx = beverage_no.index(b_no)

                    beverage_name[bdx] = input("변경할 이름(영문) : ")
                    beverage_title[bdx] = input("변경할 이름(한글) : ")
                    beverage_price[bdx] = int(input("변경할 금액 : "))
                    print("상품이 수정되었습니다.")
                else:
                    print("상품 번호가 존재하지 않습니다.")

            elif select == "3":
                print("\n[MBC 카페 디저트 상품 수정하기]")

                d_no = int(input("상품 번호 : "))

                if d_no in dessert_no:
                    ddx = dessert_no.index(d_no)

                    dessert_name[ddx] = input("변경할 이름(영문) : ")
                    dessert_title[ddx] = input("변경할 이름(한글) : ")
                    dessert_price[ddx] = int(input("변경할 금액 : "))
                    print("상품이 수정되었습니다.")

            elif select == "4":  # 처음으로 돌아가기
                subRun = False

    elif select == "6":   #회원가입 및 로그인
        print("회원가입 및 로그인 페이지입니다.")

        subRun = True

        while subRun:
            print(subMenu6)

            subChoose = input("원하시는 번호를 선택해주세요 : ")

            if subChoose == "1":
                print("[MBC 카페 로그인]")

                id = input("아이디 : ")
                pw = input("비밀번호 : ")

                if id in ids:
                    idx = ids.index(id)
                    if pws[idx] == pw:
                        session = idx
                        print(f"{ids[idx]}님 로그인 성공")

                        if groups[idx] == "admin":
                            print("▶ 관리자 계정입니다.")
                        elif groups[idx] == "manager":
                            print("▶ 매니저 계정입니다.")
                        elif groups[idx] == "staff":
                            print("▶ 직원 계정입니다.")
                        else:
                            print("▶ 일반 회원 계정입니다.")
                    else:
                        print("비밀번호가 틀렸습니다.")
                else:
                    print("존재하지 않는 아이디입니다.")

            elif subChoose == "2":   #회원가입
                print("[MBC 카페 회원가입]")

                id = input("아이디 : ")

                if id in ids:
                    print("이미 존재하는 아이디입니다.")
                    continue

                pw = input("비밀번호 : ")
                name = input("이름 : ")
                number = input("전화번호 : ")

                print("\n[입력 정보 확인]")
                print(f"이름 : {name}\n 아이디 : {id}\n 전화번호 : {number}\n")

                if input("가입하시겠습니까? (y / n) : ") == "y":
                    sns.append(len(sns)+1)   #처음에 변수둔 sns가 0번째부터 시작이면 +1하지말기
                    ids.append(id)
                    names.append(name)
                    pws.append(pw)
                    numbers.append(number)
                    groups.append("normal")
                    print("회원가입이 완료되었습니다.")
                else:
                    print("회원가입이 취소되었습니다.")


            elif subChoose == "3":   #회원수정
                print("[MBC 카페 회원정보 수정 페이지]")

                if groups[session] :
                    print("------------------------------------------------------------------")
                    print("[내 정보 수정]")
                    print(f"사번 : {sns[session]} | 이름 : {names[session]}님의 정보를 수정합니다.")
                    print("------------------------------------------------------------------")

                    names[session] = input(f"이름 : {names[session]}")
                    pws[session] = input(f"비밀번호 : {pws[session]}")
                    numbers[session] = input(f"전화번호 : {numbers[session]}")

                    print("수정이 완료되었습니다.")

            elif subChoose == "4":   #권한설정
                if session is None:
                    print("관리자만 이용할 수 있습니다. 로그인 후 이용해주세요.")
                    continue

                if groups[session] == "admin":

                    print("[MBC 카페 권한 설정 페이지]")

                    no = int(input("권한설정을 변경할 사번을 입력해주세요 : "))

                    if no in sns:
                        idx = sns.index(no)

                        sel = input(f"{names[idx]}님의 권한을 변경하시겠습니까?\n 현재 권한은 {groups[idx]}입니다.")

                        print("1. 매니저")
                        print("2. 직원")
                        print("변경하실 권한을 입력해주세요.")

                        if sel == "1":
                            print("권한이 '매니저'로 변경되었습니다.")
                        elif sel == "2":
                            print("권한이 '직원'으로 변경되었습니다.")
                        else:
                            print("잘못 입력되었습니다.")
                    else:
                        print("존재하지 않는 사번입니다.")

            elif subChoose == "5":   #돌아가기
                subRun = False

            else:
                print("잘못된 번호를 입력하셨습니다.")


    elif select == "7":
        print("[MBC 카페 홈페이지를 종료합니다.]")
        run = False

    else:
        print("잘못 입력하셨습니다.")
        print("1~7번 메뉴 중 원하시는 메뉴를 선택해주세요.")