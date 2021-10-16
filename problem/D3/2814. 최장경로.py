import sys

sys.stdin = open('input.txt')


def graph(relations, N):

    node = [[] for _ in range(N+1)]

    for relation in relations:  # 인접리스트 만들기
        n1, n2 = relation
        node[n1].append(n2)
        node[n2].append(n1)

    result = 0  # 최장 경로를 담을 변수

    def dfs(number, cnt, visited):  # 경로를 찾는 함수
        nonlocal result

        for num in node[number]:  # 현재 노드에서 갈 수 있는 노드들에 하나씩 접근
            if num in visited:  # 이미 지나왔던 곳이면 넘어감
                continue
            dfs(num, cnt + 1, visited+[num])  # 현재 노드를 방문체크 해주고 다음 노드로 넘어감

        if result < cnt:
            result = cnt
        return

    for i in range(1, N+1):
        dfs(i, 1, [i])

    return result


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    relations = [list(map(int, input().split())) for _ in range(M)]
    print('#{} {}'.format(test_case, graph(relations, N)))
