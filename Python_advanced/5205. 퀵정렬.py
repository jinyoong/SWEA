import sys

sys.stdin = open('input.txt')


def solution(numbers, end):

    if not numbers:
        return []

    p_num = numbers[0]  # 기준값(0번 원소)
    small = []  # 기준값보다 작은 수를 담을 배열
    big = []  # 기준값보다 큰 수를 담을 배열

    for i in range(1, end):  # 1번부터 끝까지 돌면서 small 과 big 배열에 추가

        if numbers[i] <= p_num:
            small.append(numbers[i])

        else:
            big.append(numbers[i])

    a = solution(small, len(small))  # 작은 값들이 모였으면 a에 저장
    b = solution(big, len(big))  # 큰 값들이 모였으면 b에 저장

    return a + [p_num] + b  # 지금까지 모인 작은 값들과 큰 값들을 순서대로 합침


def quick(left, right):
    if left >= right:
        return

    pivot = numbers[left]
    start = left+1
    end = right-1

    while start <= end:
        while start <= end and numbers[start] <= pivot:
            start += 1

        while start <= end and numbers[end] >= pivot:
            end -= 1

        if start <= end:
            numbers[start], numbers[end] = numbers[end], numbers[start]

    numbers[left], numbers[end] = numbers[end], numbers[left]

    quick(left, end)
    quick(end+1, right)


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(test_case, solution(numbers, N)[N//2]))
    quick(0, N)
    # print('#{} {}'.format(test_case, numbers[N//2]))
