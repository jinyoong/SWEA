dr = [1, 0]
dc = [0, 1]


def solution(field, row, col, result):
    global answer

    if result >= answer:
        return

    if [row, col] == [n, n-1] or [row, col] == [n-1, n]:
        if answer >= result:
            answer = result
        return

    if row >= n or col >= n:
        return

    for i in range(2):
        new_row = row + dr[i]
        new_col = col + dc[i]
        solution(field, new_row, new_col, result+field[row][col])


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(n)]
    answer = 10 * (n-1)
    solution(field, 0, 0, 0)
    print("#{} {}".format(test_case, answer))
