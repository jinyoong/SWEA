def solution(areas, last, result):
    global answer

    if visited == [1] * N:
        if result+areas[last][0] < answer:
            answer = result+areas[last][0]
        return

    if result > answer:
        return

    for i in range(1, N):
        if not visited[i] and i != last:
            visited[i] = 1
            solution(areas, i, result+areas[last][i])
            visited[i] = 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    areas = [list(map(int, input().split())) for _ in range(N)]
    answer = 10000
    result = last = 0
    visited = [1] + [0] * (N-1)
    solution(areas, last, result)
    print(f'#{test_case} {answer}')
