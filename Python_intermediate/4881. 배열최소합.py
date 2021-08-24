import sys

sys.stdin = open('input.txt')


def permutation(idx, n, used, input_list):
    global min_sum
    global ans_sum
    """
    세로줄이 겹치면 안되니까 열들의 순열을 구한다음에
    0 행 ~ n-1 행까지의 해당 열 숫자를 모두 더한 다음 최솟값을 찾아보자
    3 * 3 배열이면 열들의 순열은 [0, 1, 2], [0, 2, 1] ... 으로 나올 수 있는데
    인덱스를 행으로, 값을 열로 보고 answer 를 채우자
    """
    if idx == n:
        if min_sum > ans_sum:
            min_sum = ans_sum
        return
    elif ans_sum > min_sum:
        return

    for i in range(n):
        if not used[i]:
            temp = input_list[idx][i]
            ans_sum += temp
            used[i] = True
            permutation(idx+1, n, used, input_list)
            used[i] = False
            ans_sum -= temp
    return min_sum


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    input_list = [list(map(int, input().split())) for _ in range(n)]
    used = [False] * n
    idx = 0
    result = []
    answer = []
    min_sum = 10 * n
    ans_sum = 0
    print("#{} {}".format(test_case, permutation(idx, n, used, input_list)))
