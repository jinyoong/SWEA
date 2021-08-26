def find_start_idx(lst, n):
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 2:
                return [i, j, 0]


def maze_distance(maze, can_go):

    while can_go:  # 이동할 수 있는 점이 없어질 때까지 반복!

        cur_row, cur_col, distance = can_go.pop(0)  # 이동이 가능한 점과 해당 점까지의 거리를 뽑아온다
        visited[cur_row][cur_col] = distance + 1  # 이동 거리를 1 증가

        if maze[cur_row][cur_col] == 3:  # 만약 현재 위치가 도착점이면 이동 거리에 1을 빼서 반환
            return distance - 1

        for i in range(4):  # 좌, 상, 우, 하 순으로 이동할 수 있는 점이 있는지 확인
            new_row = cur_row + move_row[i]
            new_col = cur_col + move_col[i]
            if not(0 <= new_row < n and 0 <= new_col < n):  # 이동하려는 위치가 범위를 벗어나면 넘어가자
                continue
            if maze[new_row][new_col] != 1 and not visited[new_row][new_col]:  # 이동하려는 위치가 벽이 아니고, 한 번 지나온 곳도 아니면
                can_go.append([new_row, new_col, distance+1])  # 해당 위치에 접근할 수 있으니까 추가!

    return 0  # while 반복문이 끝날때까지 도착점에 못 가면 영영 못가니까 0 반환


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    input_list = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    start_pt = [find_start_idx(input_list, n)]  # 시작점의 행, 열, 이동한 거리가 저장
    move_row = [0, -1, 0, 1]
    move_col = [-1, 0, 1, 0]
    print('#{} {}'.format(test_case, maze_distance(input_list, start_pt)))

