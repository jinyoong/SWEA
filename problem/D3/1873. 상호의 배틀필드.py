def find_start(field):  # 탱크의 시작 위치
    for i in range(h):
        for j in range(w):
            if field[i][j] in location.keys():
                return i, j


def tank_move(field, command, r, c):  # 상, 하, 좌, 우 입력시 작동하는 함수
    if command == 'U':
        if 0 <= r - 1 < h and field[r - 1][c] == '.':
            field[r][c] = '.'
            r -= 1
        field[r][c] = '^'

    if command == 'D':
        if 0 <= r + 1 < h and field[r + 1][c] == '.':
            field[r][c] = '.'
            r += 1
        field[r][c] = 'v'

    if command == 'L':
        if 0 <= c - 1 < w and field[r][c - 1] == '.':
            field[r][c] = '.'
            c -= 1
        field[r][c] = '<'

    if command == 'R':
        if 0 <= c + 1 < w and field[r][c + 1] == '.':
            field[r][c] = '.'
            c += 1
        field[r][c] = '>'
    return r, c


def battle_field(field, commands, start_pt):
    r, c = start_pt

    for command in commands:
        if command == 'S':  # 포탄을 발사할 경우
            dr, dc = location[field[r][c]]
            new_r, new_c = r, c
            while 0 <= new_r+dr < h and 0 <= new_c+dc < w:  # 포탄이 맵 안에 있는 경우 반복
                new_r += dr
                new_c += dc
                if field[new_r][new_c] == '#':  # 강철벽을 만나면 아무 일도 일어나지 않는다
                    break
                if field[new_r][new_c] == '*':  # 돌 벽을 만나면 돌 벽을 허물어 평지로 만들고 종료
                    field[new_r][new_c] = '.'
                    break
            continue

        r, c = tank_move(field, command, r, c)  # 상, 하, 좌, 우 이동 후 좌표

    return field


T = int(input())

for test_case in range(1, T + 1):
    h, w = map(int, input().split())
    map_list = [list(input()) for _ in range(h)]
    n = int(input())
    commands = list(input())
    location = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    start_pt = find_start(map_list)
    answer = battle_field(map_list, commands, start_pt)
    print('#{}'.format(test_case), end=" ")
    for ans in answer:
        print(''.join(ans))
