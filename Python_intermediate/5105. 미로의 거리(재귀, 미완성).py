def find_start_idx(lst, n):
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 2:
                return [i, j]


def maze_distance(maze):
    if not can_go:
        return 0

    cur_row, cur_col, distance = can_go.pop(0)
    visited[cur_row][cur_col] = 1

    if maze[cur_row][cur_col] == 3:
        return distance - 1

    for i in range(4):
        new_row = cur_row + move_row[i]
        new_col = cur_col + move_col[i]
        if not(0 <= new_row < n and 0 <= new_col < n) or visited[new_row][new_col]:
            continue
        if maze[new_row][new_col] != 1:
            can_go.append([new_row, new_col, distance+1])
    return maze_distance(maze)


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    input_list = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    start_idx = find_start_idx(input_list, n) + [0]
    can_go = [start_idx]
    move_row = [0, -1, 0, 1]
    move_col = [-1, 0, 1, 0]
    print('#{} {}'.format(test_case, maze_distance(input_list)))
