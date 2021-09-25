import sys

sys.stdin = open('input.txt')


def sum_node(num):  # 비어있는 노드 값 채우기
    for i in range(2):
        temp = num * 2 + i
        if temp > n:
            continue
        if not tree[temp]:  # 자식 노드가 있는데, 값이 0인 경우
            sum_node(temp)  # 해당 자식 노드로 넘어감
        tree[num] += tree[temp]  # 자식 노드가 있고, 값도 있는 경우 더해준다


T = int(input())

for test_case in range(1, T + 1):
    n, m, result = map(int, input().split())
    tree = [0 for _ in range(n + 1)]
    for _ in range(m):
        node, value = map(int, input().split())
        tree[node] = value
    sum_node(1)
    print("#{} {}".format(test_case, tree[result]))
