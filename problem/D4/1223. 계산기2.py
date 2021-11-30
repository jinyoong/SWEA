import sys

sys.stdin = open("input.txt")


def formula(form):
    calc = {'+': 0, '*': 1}  # 우선순위를 지정해주자
    calc_stack = []  # 연산자를 담을 스택
    numbers = []  # 후위 표기식으로 담을 리스트

    # 중위 표기식을 후위 표기식으로 바꾸자
    for word in form:
        if word in calc:

            if not calc_stack:  # 연산자 스택이 비어있는 경우
                calc_stack.append(word)

            else:  # 연산자 스택이 비어있지 않은 경우
                if calc[word] <= calc[calc_stack[-1]]:  # 현재 연산자가 스택 최상단 연산자보다 우선순위 이상인 경우
                    while calc[calc_stack[-1]] >= calc[word]:  # 스택 최상단의 연산자의 우선순위가 더 작아질때까지 꺼낸다
                        numbers.append(calc_stack.pop())
                        if not calc_stack:  # 만약 스택이 중간에 비면 멈추자
                            break
                calc_stack.append(word)  # 모든 작업이 끝나면 현재 연산자를 스택에 추가
        else:
            numbers.append(int(word))  # 피연산자는 바로 후위 표기식 리스트에 추가

    while calc_stack:  # 연산자 스택에 남아있는 모든 연산자를 전부 후위 표기식 리스트에 추가
        numbers.append(calc_stack.pop())
    return numbers


def calculate(numbers):  # 후위 표기식으로 계산하기
    num = []  # 계산하는 숫자들을 담을 스택
    for alpha in numbers:
        if type(alpha) != int:  # 후위 표기식에서 연산자가 나온 경우
            n1 = num.pop()
            n2 = num.pop()
            # 두 개의 숫자를 꺼내서 해당 연산자로 연산하고 다시 추가
            if alpha == "+":
                num.append(n1 + n2)
            else:
                num.append(n1 * n2)
        else:
            num.append(alpha)
    return num[0]


for test_case in range(1, 11):
    n = int(input())
    form = input()
    numbers = formula(form)
    print("#{} {}".format(test_case, calculate(numbers)))
