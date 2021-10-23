import sys

sys.stdin = open('input.txt')


def solution(end, cnt):

    weights = [1000000] * (N + 1)
    weights[0] = 0

    for i in range(N):  # i 노드에서 출발하는 경우

        for r in road[i]:  # i 노드에서 갈 수 있는 노드들과 가중치를 하나씩 접근
            if r[1] + weights[i] < weights[r[0]]:  # i 노드에서 r[0] 노드까지 갈 때 필요한 거리가 지금까지 나온 r[0]까지의 거리보다 짧은 경우 갱신
                weights[r[0]] = r[1] + weights[i]

    return weights[-1]


T = int(input())

for test_case in range(1, T+1):
    N, E = map(int, input().split())
    road = [[] for _ in range(N+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        road[n1].append([n2, w])
    print('#{} {}'.format(test_case, solution(N, E)))
