# __all__ 내장 변수

# __init__.py 파일이 있는 상태에서
# from game.sound import * (하위 모든 것)
#           패키지
# echo.echo_test()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'echo' is not defined
# echo라는 이름이 정의되지 않았다라는 오류가 나옴
# *을 사용하고 싶으면 2가지 해결방법이 있음.
# 1. __init__.py 파일을 만들지 말것.(그러면 패키지가 아님)
# 2. __init__.py 파일 안에 __all__을 이용해서 제공할 것.

__all__ = ["echo"]  # 변수에 리스트화하여 모듈을 넣음.
#           echo.py
# __all__이 의미하는 것은 sound 패키지 하위 모듈을 import할 목록임.

# 이때 착각하기 쉬운 것은
# from game.sound.echo import *은 __all__에 상관없이 import 하는 용도.
#                 모듈
# 패키지의 모든 건 초기화됨. 따라서 all 사용.
# 모듈의 전부는 함수이기 때문에 위의 함수처럼 사용하면 가능함.
# from game.sound import * 은 패키지를 *로 import해서 __init__.py에 영향을 받음.
#            패키지
