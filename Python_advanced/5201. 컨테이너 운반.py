def solution(containers, trucks):
    answer = 0

    containers.sort(reverse=True)

    for truck in trucks:
        for i in range(N):
            if containers[i] and truck >= containers[i]:
                answer += containers[i]
                containers[i] = 0
                break

    return answer


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    print(f'#{test_case} {solution(containers, trucks)}')
