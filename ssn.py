# 주민번호를 입력 받아 생년월일 남녀 구분을 하는 코드
# input() 함수를 사용하면 콘솔로 데이터를 넣을 수 있다.
# 처리0 : 주민번호 입력 검증 -> 14글자인지/ 7번째에 있는지 - 유무
# 처리1 : 생년월일을 추출하자 -> 1,2,5,6 1900년생, 나머지 2000년생
# 처리2 : 주민번호 8번째 글자를 추출 -> 남여구분
# 처리3 : 9~10번째 글자를 추출 -> 출생지역

print("주민번호를 입력하세요!(-포함 14자)")
ssn = input(">>>")
# 입력된 주민번호 검증 코드
if len(ssn) == 14 : #키보드로 입력된 문자열이 14자인지?
    print("14자 입력이 확인되었습니다.")
else:
    print("주민번호 14자가 입력되지 않았습니다.")
    exit(0) #강제 종료 됨.

if ssn[6] == "-" :
    print("주민번호 7번째 구문자 인식완료")
else:
    print("주민번호 7번째 구문자가 입력되지 않았습니다.")
    print("프로그램을 처음부터 다시 실행하세요.")
    exit(0)  #강제 종료 됨.

print("입력된주민번호 :"+ssn)
# 주민번호 앞 6자리를 생년월일로 추출 -> 1,2,5,6 1900년생
# 나머지는 2000년생

year = ssn[0:2] #생년
month = ssn[2:4] #생월
day = ssn[4:6] #생일

#1900년생인지 2000년생인지 구분하기 위한 코드(변수를 미리 만드는게 좋음)
fullYear = "" #if안쪽에서 변수를 만들면 버그가 생길 수 있어서 미리 만듬
# "" null 처리용(빈칸용)
if ssn[7] in ["1","2","5","6"] : #for문 대신 사용(반복문)
    fullYear = "19"+year
else :
    fullYear = "20"+year
print("귀하의 생년은 : " + fullYear + "년생 입니다.")

# 나이계산 해보자
age = 2026 - int(fullYear)
print("귀하의 나이는 " + str(age) + "세 입니다.") #확실하게 계산하려면 괄호 치고, int는 숫자로 바꿔줘야하니까 넣기
#                      print는 문자열+슷자로 출력오류 발생
#                      문자열로 변환(강제타입변환) -> str(age)로 변환

# 주민번호 8번째 숫자가 1,3,5,7이면 남자, 나머지는 여자
gender = "" #성별 null 변수 선언
if ssn[7] in ["1","3","5","7"] : #표안에있는걸 비교할땐 in, ==은 동등하게 비교할때 사용
    gender = "남성"
elif ssn[7] == "9" :
    gender = "외계인"
else:
    gender = "여성"
print("귀하는 " + gender + "(으)로 판단됩니다.")

local = "" #출생지역을 판단하는 문자열
ssnLocal = ssn[8:10] #출생지 코드 추출

if int(ssnLocal) <= 8 :
    local = "서울"
elif int(ssnLocal) <= 12 :
    local = "부산"
elif int(ssnLocal) <= 15 :
    local = "인천"
elif int(ssnLocal) <= 25 :
    local = "경기"
elif int(ssnLocal) <= 34 :
    local = "강원"
elif int(ssnLocal) <= 47 :
    local = "충청"
elif int(ssnLocal) <= 66 :
    local = "전라"
elif int(ssnLocal) <= 91 :
    local = "경상"
elif int(ssnLocal) <= 95 :
    local = "제주"
print("귀하의 출생지는 " + local + "입니다.")


# 연습
# sex = ""
# if ssn[7] in ["1","3","5","7"] :
#     sex = "남자"
# else:
#     sex = "여자"
# print("귀하의 성별은 : " + sex + "입니다.")

