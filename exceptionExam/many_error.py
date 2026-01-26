# 예외가 이것저것 날 것 같을 때?
# try문 안에서 여러개의 오류를 처리

try :
    4 / 0
    a = [1, 2]
    print(a[3])

# except ZeroDivisionError as e :
#     print(e)
#     print("0으로 나눠지는 예외가 발생함.")
#
# except IndexError as e :
#     print(e)
#     print("리스트 인덱스 범위 초과")

# 4/0이 결과 도출이 안되는 이유는
# print(a[3])이 먼저 프린트 되면서 error코드가
# 먼저 결과로 나왔기 때문에 4/0에 대한 error코드는 나오지 않음
# 4/0에 대한 결과값을 나오게 하고싶으면 finally를 써야함

except (ZeroDivisionError, IndexError) as e :
    print(e)
    print("0으로 나눴거나 리스트의 범위 초과 예외 발생!")
    print("예외 발생 시 담당자에게 문의하세요 : (전화번호)")