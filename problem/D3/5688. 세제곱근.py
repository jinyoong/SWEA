def solution():
    '''
    1 <= N <= 10 ^ 18 이므로 세제곱근의 범위는 1 <= X <= 10 ^ 6(1000000) 까지
    x ^ 3 = a 라 하면
    (x + 1) ^ 3 = x ^ 3 + 3 * x ^ 2 + 3 * x + 1 = a + 3 * x ^ 2 + 3 * x + 1
    '''
    result = [1] * 1000001
    result[0] = 0

    for i in range(2, 1000001):
        result[i] = result[i-1] + 3 * ((i-1) ** 2) + 3 * (i-1) + 1

    return result


T = int(input())

n_lst = solution()

for test_case in range(1, T+1):
    N = int(input())
    answer = 0
    try:
        answer = n_lst.index(N)
    except:
        answer = -1

    print(f'#{test_case} {answer}')
