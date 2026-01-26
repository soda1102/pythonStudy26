# 주민번호를 입력 받아 생년월일 남녀 구분을 하는 코드
# input() 함수를 사용하면 콘솔로 데이터를 넣을 수 있다.
# 처리0 : 주민번호 입력 검증 -> 14글자인지/ 7번째에 있는지 - 유무
# 처리1 : 생년월일을 추출하자 -> 1,2,5,6 1900년생, 나머지 2000년생
# 처리2 : 주민번호 8번째 글자를 추출 -> 남여구분
# 처리3 : 9~10번째 글자를 추출 -> 출생지역

#011102-412 3 4 5 6
#012345678910111213

print("주민번호를 입력하세요!(-포함 14글자)")
ssn = input(">>>")
if len(ssn) == 14 :
    print("주민번호 14자리 입력이 확인되었습니다.")
else:
    print("주민번호 14자리 입력이 확인되지 않았습니다.")
    exit(0)

if ssn[6] == "-" :
    print("주민번호 구문자 입력 인식 완료")
else:
    print("주민번호 구문자 입력 인식 안됨")
    print("처음부터 다시 입력해주세요.")
    exit(0)

print("입력된 주민번호 :" +ssn)

year = ssn[0:2]
month = ssn[2:4]
day = ssn[4:6]

fullYear = ""
if ssn[7] in ["1","2","5","6"] :
    fullYear = "19" + year
else:
    fullYear = "20" + year
print("귀하의 생년은 " + fullYear + "년 입니다.")

age = 2026 - int(fullYear)
print("귀하의 나이는 " + str(age) + "세 입니다.")

gender = ""
if ssn[7] in ["1","3","5","7"] :
    gender = "남자"
else :
    gender = "여자"
print("귀하의 성별은 " + gender + "입니다.")

local = ""
ssnLocal = ssn[8:10]
if int(ssnLocal) <=8 :
    local = "서울"
elif int(ssnLocal) <=12 :
    local = "부산"
elif int(ssnLocal) <=15 :
    local = "인천"
elif int(ssnLocal) <=25 :
    local = "경기"
elif int(ssnLocal) <=34 :
    local = "강원"
elif int(ssnLocal) <=47 :
    local = "충청"
elif int(ssnLocal) <=66 :
    local = "전라"
elif int(ssnLocal) <=91 :
    local = "경상"
elif int(ssnLocal) <=95 :
    local = "제주"
print("귀하의 출생지는 " + local + "입니다.")
exit(0)



ssn = "011102-4431236"
#      0123456789

s1 = int(ssn[0]) * 2 + int(ssn[1]) * 3 + int(ssn[2]) * 4 +  int(ssn[3]) * 5 + int(ssn[4]) * 6 + int(ssn[5]) * 7 + int(ssn[7]) * 8 + int(ssn[8]) * 9 + int(ssn[9]) * 2 + int(ssn[10]) * 3 + int(ssn[11]) * 4 + int(ssn[12]) * 5
print(s1)

s2 = s1 % 11
print(s2)

s3 = 11 - s2
print(s3)





