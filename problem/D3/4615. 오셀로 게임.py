import sys

sys.stdin = open('4615.txt')


def solution(game_list, N):
    '''
    돌을 놓을 수 있는 곳만 좌표로 주어지는게 힌트!!
    그리고 돌의 좌표는 2차원 배열의 행, 열 기준과 반대
    '''
    field = [[0] * (N+1) for _ in range(N+1)]
    mid = N//2
    field[mid][mid] = field[mid+1][mid+1] = 2  # 시작위치에 백돌 2개를 놓는다
    field[mid+1][mid] = field[mid][mid+1] = 1  # 시작위치에 흑돌 2개를 놓는다

    # 북, 북동, 동, 동남, 남, 남서, 서, 서북 순으로!
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for ele in game_list:
        row, col = ele[1], ele[0] # 기준축이 반대!

        field[row][col] = ele[2]

        for i in range(8):
            new_r = row + dr[i]
            new_c = col + dc[i]

            check = []
            while True:

                if new_r < 1 or new_r > N or new_c < 1 or new_c > N:
                    break

                if field[new_r][new_c] in (ele[2], 0):  # 해당 방향이 현재 돌이거나 아무것도 없는 경우
                    if check and field[new_r][new_c] == ele[2]:
                        for point in check:
                            field[point[0]][point[1]] = ele[2]
                    break

                # 해당 방향에 놓인 돌이 현재 놓은 돌이 아닌 경우
                check.append([new_r, new_c])
                new_r += dr[i]
                new_c += dc[i]

    white_ct = black_ct = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if field[i][j] == 2:
                white_ct += 1
            elif field[i][j] == 1:
                black_ct += 1

    return black_ct, white_ct


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    game_list = [list(map(int, input().split())) for _ in range(M)]
    print("#{}".format(test_case), *solution(game_list, N))
