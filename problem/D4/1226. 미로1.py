def find_start(lst):  # 시작 인덱스를 구하자
    for i in range(16):
        for j in range(16):
            if lst[i][j] == 2:
                return [i, j]


def is_escape(maze, can_go):
    if not can_go:  # 만약 더 갈 수 있는 점이 없으면 0 반환
        return 0

    cur_row, cur_col = can_go.pop(0)  # can_go 에서 가능성을 탐색할 위치를 뽑는다
    visited[cur_row][cur_col] = 1  # 현재 위치는 다시 탐색할 수 없게 표시

    if maze[cur_row][cur_col] == 3:  # 도착점이 되면 1 반환
        return 1

    for i in range(4):  # 좌, 상, 우, 하 순으로 가능성이 있는 점을 탐색
        new_row = cur_row + move_row[i]  # 해당 방향으로 이동한 점을 저장
        new_col = cur_col + move_col[i]
        if maze[new_row][new_col] == 1 or visited[new_row][new_col]:  # 이동한 점이 벽이거나, 이미 지나간 길인 경우는 넘어간다
            continue
        can_go.append([new_row, new_col])  # 가능성이 있는 점들을 can_go에 저장
    return is_escape(maze, can_go)


for _ in range(10):
    test_case = int(input())
    input_list = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    start_pt = [find_start(input_list)]
    move_row = [0, -1, 0, 1]
    move_col = [-1, 0, 1, 0]
    print('#{} {}'.format(test_case, is_escape(input_list, start_pt)))
