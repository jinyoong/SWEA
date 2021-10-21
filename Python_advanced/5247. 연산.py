import sys

sys.stdin = open('input.txt')


def solution(start, goal):

    queue = [[]]
    queue[0] = [start, 0]
    head = 0
    length = 1
    maked = {start}

    while head < length:
        num, cnt = queue[head]
        head += 1

        if num == goal:
            return cnt

        new = [num + 1, num - 1, num * 2, num - 10]
        cnt += 1

        for i in range(4):
            if new[i] > 1000000 or new[i] <= -2:
                continue
            if new[i] in maked:
                continue
            maked.add(new[i])
            queue += [[new[i], cnt]]
            length += 1


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    print('#{} {}'.format(test_case, solution(N, M)))
