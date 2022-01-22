def solution(immigration, M):

    answer = 0

    for i in range(M):
        pass

    return immigration


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    immigration = [int(input()) for _ in range(N)]
    immigration.sort()
    print('#{} {}'.format(test_case, solution(immigration, M)))
