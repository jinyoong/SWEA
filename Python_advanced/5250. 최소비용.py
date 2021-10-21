import sys

sys.stdin = open('input.txt')


def solution(heights):

    temp_lst = [[1000000] * N for _ in range(N)]  # 처음에 1000 으로 둬서 계속 실패!
    temp_lst[0][0] = 0

    queue = [[0, 0]]
    head = 0
    rear = 1

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while head < rear:
        row, col = queue[head]
        head += 1
        start = heights[row][col]  # 현재 출발하는 곳의 높이

        for i in range(4):  # 현재 점부터 주변 4 방향 탐색
            new_row = row + dr[i]
            new_col = col + dc[i]

            if new_row < 0 or new_row >= N or new_col < 0 or new_col >= N:  # 범위를 벗어나면 다음으로
                continue

            goal = heights[new_row][new_col]  # 현재 가려는 곳의 높이
            distance = 1  # 기본 연료 소비량

            if goal > start:  # 가려는 곳의 높이가 더 큰 경우
                distance += (goal - start)

            # 현재까지 계산된 가려는 곳의 연료 소비량보다 지금 계산한 연료 소비량이 더 작은 경우 갱신
            if temp_lst[new_row][new_col] > temp_lst[row][col] + distance:
                temp_lst[new_row][new_col] = temp_lst[row][col] + distance
                queue.append([new_row, new_col])
                rear += 1

    return temp_lst[N-1][N-1]


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(test_case, solution(H)))
