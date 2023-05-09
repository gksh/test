# 계산기 함수 정의
def calculator():
    # 사용자 입력 받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    operator = input("연산자를 입력하세요 (+, -, *, /): ")
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    # 연산 결과 계산
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("잘못된 연산자입니다.")
        return

    # 결과 출력
    print(f"{num1} {operator} {num2} = {result}")


# 계산기 실행
while True:
    calculator()
    answer = input("다른 계산을 하시겠습니까? (Y/N): ")
    if answer.upper() == "N":
        break
