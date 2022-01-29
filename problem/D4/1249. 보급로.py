import sys

sys.stdin = open('s_1294.txt')


def solution(work):
    # 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    temp = [[999999] * N for _ in range(N)]
    temp[0][0] = 0

    queue = [[0, 0]]
    head = 0
    rear = 1

    while head < rear:

        r, c = queue[head]
        head += 1

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if temp[nr][nc] <= temp[r][c] + work[nr][nc]:
                continue

            temp[nr][nc] = temp[r][c] + work[nr][nc]
            queue.append([nr, nc])
            rear += 1

    return temp[-1][-1]


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    work = [list(map(int, input())) for _ in range(N)]
    print('#{} {}'.format(test_case, solution(work)))
