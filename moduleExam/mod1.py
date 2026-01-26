# 모듈 학습하기
# 모듈은 파이썬 파일로 만든 것을 연동하여 프로그램으로 처리
# 실무에서는 파일 1개로 모두 만들어 제공하는 것이 아니라
# 각각 기능이 있는 파일을 빼서 클래스화 하고 메서드로 동작한다.

# main_practice.py -> __name__ (__main__) 주 실행 코드와 서비스를 연결하는 주메뉴와 메서드
# MemberService_practice.py -> __name__ (MemnerService) 회원 관리하는 클래스와 메서드
# ScoreService_practice.py -> __name__ (ScoreService) 성적 관리하는 클래스와 메서드
# BoardService.py -> __name__ (BoardService) 게시판을 관리하는 클래스와 메서드
# ItemService.py -> __name__ (ItemService) 상품을 관리하는 클래스와 메서드
# CartService.py -> __name__ (CartService) 장바구니를 관리하는 클래스와 메서드

# 파이썬확장자.py로 만든 파이썬 파일은 모두 모듈로 처리 가능함.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

# print(add(1,4))
# print(sub(4,2))
# 터미널에 python을 실행하고 import mod1을 했더니
# 바로 프린트 문이 실행된다.
# 당연한 결과지만 main에서 실행하면 ?
# mod1.py에서 print 2개가 실행되고
# main.py에서 print 2개가 실행된다.
# main에서는 add와 sub 함수만 호출해서 사용하려고만 한것임.

if __name__ == '__main__':
    # 클래스나 모듈이 호출된 자신이 main 역할인지를 확인하는 것
    print(add(3,4))
    print(sub(3,4))

print(__name__)  # mod1