b = input("사용할 변수 이름??")
import keyword
num = "0123456789"
b1 = b[0:1]
if b in keyword.kwlist:
    print("사용할 수 없음")
elif not b.isalnum():
    if "_" in b:
        print("사용가능")
    elif b=="":
        print("이름을 입력하세요!")
    else:
        print("사용할 수 없음! special!")
