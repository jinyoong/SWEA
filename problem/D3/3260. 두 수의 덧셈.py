def same_len(x, y):  # 더 짧은 숫자 앞에 0을 채워서 길이를 똑같이 맞춰주자
    if len(x) > len(y):
        y = '0' * (len(x) - len(y)) + y
    elif len(x) < len(y):
        x = '0' * (len(y) - len(x)) + x
    return x, y


def n_sum(num1, num2, idx, plus):  # 자릿수별로 하나씩 구하고 올림수를 구하자
    global result
    if idx == -(len(num1)+1):  # 맨 앞 숫자까지 모두 더했을 경우
        if plus:  # 올림수가 남아있다면, 1 + 9 같은 경우니까 앞에 올림수 추가
            result = str(plus) + result
        return

    sum_num = int(num1[idx]) + int(num2[idx]) + plus  # 현재 자리 숫자 2개와 그 전 연산에서 구해진 올림수 더하기
    temp1 = sum_num // 10  # 올림수 구하기
    temp2 = sum_num % 10
    result = str(temp2) + result
    n_sum(num1, num2, idx-1, temp1)


T = int(input())

for test_case in range(1, T + 1):
    n1, n2 = input().split()
    new_n1, new_n2 = same_len(n1, n2)
    result = ''
    n_sum(new_n1, new_n2, -1, 0)
    print('#{} {}'.format(test_case, result))
