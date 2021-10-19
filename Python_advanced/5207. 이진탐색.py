import sys

sys.stdin = open('input.txt')


def solution(num, start, end, side):  # side 는 전에 이동한 구역이 왼쪽인지 오른쪽인지 저장 => 0: 왼쪽, 1: 오른쪽, 2: 초기값

    if start > end:
        return 0

    mid = (start+end)//2

    if A[mid] > num:  # 가운데 숫자가 찾는 숫자보다 큰 경우 => 왼쪽으로 넘어가본다
        if side == 0:  # 이전에도 왼쪽으로 넘어갔던 경우
            return 0  # 번갈아 가지 못했으니까 0 리턴
        return solution(num, start, mid-1, 0)

    elif A[mid] < num:  # 가운데 숫자가 찾는 숫자보다 작은 경우 => 오른쪽으로 넘어가본다
        if side == 1:  # 이전에도 오른쪽으로 넘어갔던 경우
            return 0  # 번갈아 가지 못했으니까 0 리턴
        return solution(num, mid+1, end, 1)

    else:
        return 1


def binary_search_while(key):  # 유튜브 라이브 코드
    l = 0
    r = N-1
    d = -1

    while l <= r:
        mid = (l+r)//2

        if key == A[mid]:
            return 1

        elif key < A[mid]:
            if d == 0:
                return 0
            r = mid - 1
            d = 0

        else:
            if d == 1:
                return 1
            l = mid + 1
            d = 1


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    answer = 0
    for num in B:
        answer += solution(num, 0, N-1, 2)
    print('#{} {}'.format(test_case, answer))
