import sys

sys.stdin = open('5202.txt')


def solution(times):
    start = 0
    answer = idx = 0
    choiced = [0] * N

    while True:

        stop = True
        finish = 24

        for i in range(N):
            if choiced[i]:
                continue

            if times[i][0] < start:
                choiced[i] = 1
                continue

            if times[i][1] <= finish:
                finish = times[i][1]
                idx = i
                stop = False

        if stop:
            break

        answer += 1
        start = finish
        choiced[idx] = 1

    return answer


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case} {solution(times)}')
