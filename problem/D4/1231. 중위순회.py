import sys

sys.stdin = open('input.txt')


def in_order(number):  # 중위순회로 접근
    global result
    if number <= node_len:
        in_order(number * 2)  # 왼쪽 자식 노드로!
        result += node_list[number]  # 부모 노드
        in_order(number * 2 + 1)  # 오른쪽 자식 노드로!


for test_case in range(1, 11):
    node_len = int(input())
    node_list = [''] * (node_len + 1)  # 노드 번호와 값을 담을 리스트
    result = ''  # 결과를 저장할 변수
    for _ in range(node_len):
        node = list(input().split())
        node_num, node_value = int(node[0]), node[1]
        node_list[node_num] = node_value
    in_order(1)
    print('#{} {}'.format(test_case, result))
