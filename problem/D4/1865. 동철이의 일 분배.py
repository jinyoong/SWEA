import sys

sys.stdin = open('input.txt')


def solution(idx, result):
    global answer

    if result < answer:
        return

    if idx == N:
        answer = result
        return

    for i in range(N):
        if used[i] or percents[idx][i] == 0:
            continue
        used[i] = 1
        solution(idx+1, result*(percents[idx][i]/100))
        used[i] = 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    percents = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    answer = 0
    solution(0, 1)
    print('#{} {:.6f}'.format(test_case, answer * 100))
