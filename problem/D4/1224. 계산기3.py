import sys

sys.stdin = open("input.txt")


def postfix(words):
    calc = {'+': 1, '*': 2, '(': 0}  # 우선순위를 지정해주자
    calc_stack = []  # 연산자를 담을 스택
    numbers = []  # 후위 표기식으로 담을 리스트

    # 중위 표기식을 후위 표기식으로 바꾸자
    for word in words:
        if word in calc:
            if not calc_stack:  # 연산자 스택이 비어있으면 연산자 추가
                calc_stack.append(word)
            else:  # 연산자 스택이 비어있지 않은 경우
                if word == "(":  # 여는 괄호면 추가
                    calc_stack.append(word)
                else:  # 여는 괄호가 아니면 => +, * 이면
                    if calc[word] > calc[calc_stack[-1]]:  # 넣으려는 연산자의 우선순위가 더 높으면 그냥 추가
                        calc_stack.append(word)
                    else:  # 넣으려는 연산자의 우선순위가 작거나 같으면
                        while not calc_stack or calc[word] <= calc[calc_stack[-1]]:  # 더 커질때까지 추출!
                            numbers.append(calc_stack.pop())
                        calc_stack.append(word)
        elif word == ')':
            while calc_stack[-1] != '(':
                numbers.append(calc_stack.pop())
            calc_stack.pop()
        else:
            numbers.append(int(word))

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
    words = input()
    numbers = postfix(words)
    print("#{} {}".format(test_case, calculate(numbers)))
