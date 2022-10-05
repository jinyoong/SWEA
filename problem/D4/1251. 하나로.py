import sys

sys.stdin = open('1251.txt')


def solution(adj_lst, e):

    checked = [0] * N  # 방문체크용 리스트
    checked[0] = 1
    length = 0

    while checked != [1] * N:

        min_d = float('inf')
        min_p = 0

        for i in range(N):  # 출발할 섬들을 고르는 반복문
            if not checked[i]:  # 출발지가 될 수 있는 섬들은 이미 방문한 섬들
                continue
            for j in range(N):  # 도착할 섬들을 고르는 반복문
                if checked[j]:  # 방문한 적 있으면 패스
                    continue
                if adj_lst[i][j] < min_d:  # i 섬부터 j 섬까지의 거리가 현재 최소 거리보다 작은 경우 업데이트
                    min_d = adj_lst[i][j]
                    min_p = j

        length += min_d
        checked[min_p] = 1

    return round(length * e)


def make_adj():  # 길이의 제곱을 담은 인접행렬 만들기

    adj_lst = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if adj_lst[i][j]:
                continue
            garo = islands[i][0] - islands[j][0]
            sero = islands[i][1] - islands[j][1]
            distance = garo ** 2 + sero ** 2
            adj_lst[i][j] = adj_lst[j][i] = distance

    return adj_lst


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    islands = list(zip(x, y))
    adj_lst = make_adj()
    print(f'#{test_case} {solution(adj_lst, E)}')
