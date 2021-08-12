# 재귀함수로 부분집합 합 구하기

import sys

sys.stdin = open("input.txt")


def subset(now, count, total):
    if count == n:
        answer = 0
        for element in result:
            answer += element
        if answer == k:
            total += 1
        return total

    for i in range(now, 12):
        if candidate[i] == 0:
            result[count] = i + 1
            candidate[i] = 1
            total = subset(now + 1, count + 1, total)
            candidate[i] = 0

    return total

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    candidate = [0] * 12
    result = [0] * n
    print("#{} {}".format(test_case, subset(0, 0, 0)))