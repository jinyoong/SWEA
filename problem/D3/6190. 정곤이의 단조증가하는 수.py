import sys

sys.stdin = open('input.txt')


def is_mono_inc(num1, num2):  # 두 수의 곱이 단조 증가하는 수인지 확인
    number = str(num1 * num2)
    n_len = len(number)
    for i in range(n_len-1):
        if number[i] > number[i+1]:
            return False
    return int(number)


def multi(numbers, n):  # 숫자들의 곱 중 단조증가 수의 최대값 반환
    result = 0
    for i in range(n-1):
        if numbers[i] % 10 == 0:  # 만약 한 수라도 10이면 단조증가는 나올 수 없다
            continue
        for j in range(i+1, n):  # i 번째 수와 곱할 수 있는 수는 i+1 ~ n-1 번째 수
            new_num = is_mono_inc(numbers[i], numbers[j])  # 두 수를 곱해서 단조증가인지 아닌지 확인
            if not new_num:
                continue
            if result < new_num:
                result = new_num

    if result:
        return result

    return -1  # 단조증가하는 수가 없다


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(test_case, multi(numbers, n)))
