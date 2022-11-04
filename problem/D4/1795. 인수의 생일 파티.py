import sys

sys.stdin = open('s_1795.txt')


def solution(house, start):

    sum_lst = [0] * (N+1)
    go_lst = go()
    back_lst = back()

    for i in range(1, N+1):
        sum_lst[i] = go_lst[i] + back_lst[i]

    return max(sum_lst)


def go():  # 각 집에서 X로 가는 최소 거리들 구하기

    go_lst = [0] * (N+1)

    for i in range(1, N+1):

        if i == X:  # X 집에서 출발하는 경우는 볼 필요 X
            continue

        temp = [99999] * (N+1)
        temp[i] = 0  # 출발하는 집을 일단 0으로 두고 시작

        queue = [i]
        head = 0
        rear = 1

        while head < rear:

            cur = queue[head]
            head += 1

            for ele in house[cur]:

                g, t = ele

                if temp[g] <= temp[cur] + t:
                    continue

                temp[g] = temp[cur] + t
                queue.append(g)
                rear += 1

        go_lst[i] = temp[X]

    return go_lst


def back():

    temp = [99999] * (N+1)
    temp[X] = temp[0] = 0

    queue = [X]
    head = 0
    rear = 1

    while head < rear:

        cur = queue[head]
        head += 1

        for ele in house[cur]:

            g, t = ele

            if temp[g] <= temp[cur] + t:
                continue

            temp[g] = temp[cur] + t
            queue.append(g)
            rear += 1

    return temp


T = int(input())

for test_case in range(1, T+1):
    N, M, X = map(int, input().split())
    house = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        house[x].append((y, c))
    print('#{} {}'.format(test_case, solution(house, X)))
