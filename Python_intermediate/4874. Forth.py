import sys

sys.stdin = open('input.txt')


def forth(calc):
    calc_list = ['+', '*', '/', '-']
    num_stack = []
    for degree in calc:
        if degree == '.':  # 만약 . 이면 끝나므로 숫자를 출력
            if len(num_stack) != 1:
                return 'error'
            return num_stack[-1]
        elif degree not in calc_list:  # 숫자면 그냥 스택에 추가한다
            num_stack.append(int(degree))
        else:  # 만약 연산자면 연산을 진행해야 한다
            if len(num_stack) <= 1:  # 스택의 숫자가 1개 이하이면 연산을 할 수 없다
                return 'error'
            else:
                n2 = num_stack.pop()  # 연산을 위해 숫자 두 개를 뽑는다
                n1 = num_stack.pop()  # 나누기와 빼기를 위해서 순서를 고려해서 뽑는다
                if degree == calc_list[0]:
                    new_num = n1 + n2
                elif degree == calc_list[1]:
                    new_num = n1 * n2
                elif degree == calc_list[2]:
                    new_num = n1 // n2
                else:
                    new_num = n1 - n2
                num_stack.append(new_num)


T = int(input())

for test_case in range(1, T + 1):
    calc = list(input().split())
    print('#{} {}'.format(test_case, forth(calc)))
