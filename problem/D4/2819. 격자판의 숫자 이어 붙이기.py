import sys

sys.stdin = open('input.txt')

# 상 우 하 좌 순서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def solution(board, row, col, temp):
    global answer

    if len(temp) == 7:
        if temp not in total:
            answer += 1
            total.add(temp)
        return

    for i in range(4):
        new_row = row + dr[i]
        new_col = col + dc[i]

        if new_row < 0 or new_row >= 4 or new_col < 0 or new_col >= 4:
            continue

        solution(board, new_row, new_col, temp+board[row][col])


T = int(input())

for test_case in range(1, T+1):
    board = [list(input().split()) for _ in range(4)]
    answer = 0
    total = set()
    start = [(i, j) for i in range(4) for j in range(4)]
    for row, col in start:
        solution(board, row, col, '')
    print('#{} {}'.format(test_case, answer))
