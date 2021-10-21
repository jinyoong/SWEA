import sys

sys.stdin = open('input.txt')


def prim(nodes):

    checked = [0]

    a = {i for i in range(1, V+1)}
    result = 0

    while a:

        temp = checked[:]  # 선택한 정점들을 담은 변수
        min_value = 10
        value = []

        for check in temp:  # 정점들을 모두 선택해서 인접 정점들을 확인

            for node in nodes[check]:  # 현재 보고 있는 정점과 인접한 정점들 중 가중치가 가장 작은 정점 선택
                if node[0] in a and node[1] <= min_value:  # 아직 가 본 적 없는 정점이면서, 최솟값보다 작은 간선의 경우
                    value = node
                    min_value = value[1]

        a.remove(value[0])
        checked.append(value[0])

        result += value[1]

    return result


T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    nodes = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        nodes[n1].append([n2, w])
        nodes[n2].append([n1, w])
    print('#{} {}'.format(test_case, prim(nodes)))