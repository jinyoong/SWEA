import sys

sys.stdin = open('input.txt')


def cb_tree(n):  # 루트 노드에 저장된 값과, n/2 번 노드에 저장된 값 반환
    """
    중위순회로 값이 증가하는 듯
    """
    result = [0]

    def inorder(i):  # 중위순회로 각 숫자가 들어갈 노드 번호를 순서대로 넣자
        if i <= n:
            inorder(i * 2)
            result.append(i)
            inorder(i * 2 + 1)

    inorder(1)

    answer = [result.index(1), result.index(n//2)]

    return answer


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    print("#{}".format(test_case), *cb_tree(n))
