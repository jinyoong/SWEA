import sys

sys.stdin = open('input.txt')


def make_tree(nodes):  # 트리로 만들기
    tree = [[0, 0, 0] for _ in range(E+2)]

    for node in nodes:
        parants = node[0]
        child = node[1]

        for i in range(1, 3):
            if not tree[parants][i]:  # 자식노드를 하나씩 채우자
                tree[parants][i] = child
                break

        tree[child][0] = parants  # 그리고 자식 노드를 기준으로 했을 때의 부모노드도 채우자

    return tree


def subtree(N):  # 서브트리의 노드 수 찾기
    global answer
    for i in range(1, 3):  # 현재 노드의 자식 노드들을 모두 탐색
        if tree[N][i]:  # 자식 노드가 있으면
            new_node = tree[N][i]  # 해당 노드로 건너간다
            answer += 1
            subtree(new_node)
    return


T = int(input())

for test_case in range(1, T+1):
    E, N = map(int, input().split())
    numbers = list(map(int, input().split()))
    nodes = [[numbers[2*i], numbers[2*i+1]] for i in range(E)]
    tree = make_tree(nodes)
    answer = 1
    subtree(N)
    print("#{} {}".format(test_case, answer))
