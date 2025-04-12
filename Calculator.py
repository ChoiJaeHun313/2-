def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == '__main__':
    
    print('\n첫번째 숫자를 입력하세요.')
    input1 = float(input('입력: '))  # 숫자로 변환

    print('\n원하는 사칙연산 기호 중 하나를 선택하세요. (+, -, *, /)')
    act = input('기호: ')

    print('\n두번째 숫자를 입력하세요.')
    input2 = float(input('입력: '))  # 숫자로 변환

    # 연산 실행
    if act == '+':
        result = plus(input1, input2)
    elif act == '-':
        result = minus(input1, input2)
    elif act == '*':
        result = mul(input1, input2)
    elif act == '/':
        # 0으로 나누는 경우 처리
        if input2 == 0:
            result = '오류: 0으로 나눌 수 없습니다.'
        else:
            result = divide(input1, input2)
    else:
        result = '오류: 올바른 연산 기호를 입력해주세요.'

    print(f'사칙연산 결과는 {result}입니다.')
