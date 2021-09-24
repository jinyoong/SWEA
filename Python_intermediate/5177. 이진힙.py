import sys

sys.stdin = open('input.txt')


def min_heap(numbers):  # 문제에서 요구하는 힙 구조를 만들기

    idx = 1
    for num in numbers:
        heap[idx] = num  # 일단 현재 인덱스에 숫자를 넣자
        temp = 1  # 모든 노드들이 부모 노드 < 자식 노드 관계를 만족해야 하니까 처음부터 보자
        while temp <= idx // 2:  # 채워져있는 노드까지 진행
            for i in range(2):
                if temp * 2 + i > idx:  # 현재 채워진 노드의 범위를 넘어가면 넘어간다
                    continue
                if heap[temp] >= heap[temp * 2 + i]:  # 만약 부모 노드의 값이 자식 노드보다 크면 위치 바꾸기
                    heap[temp], heap[temp * 2 + i] = heap[temp * 2 + i], heap[temp]
            temp += 1
        idx += 1

    answer = 0
    last_node = n // 2

    while last_node != 0:  # 조상 노드의 합 구하기
        answer += heap[last_node]
        last_node //= 2

    return answer


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    heap = [0 for _ in range(n + 1)]  # 힙 트리를 담을 배열
    print("#{} {}".format(test_case, min_heap(numbers)))
