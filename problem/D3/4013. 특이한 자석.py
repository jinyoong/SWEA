def solution(magnets, target, direct):
    check = [0, 0, 0, 0, 0]
    queue = [[target, direct]]

    while queue:
        idx, d = queue.pop(0)
        check[idx] = 1

        left = magnets[idx][6]
        right = magnets[idx][2]

        if idx >= 2 and not check[idx-1] and magnets[idx-1][2] != left:
            queue.append([idx-1, -d])

        if idx <= 3 and not check[idx+1] and magnets[idx+1][6] != right:
            queue.append([idx+1, -d])

        if d == -1:
            magnets[idx] = magnets[idx][1:] + [magnets[idx][0]]

        if d == 1:
            magnets[idx] = [magnets[idx][-1]] + magnets[idx][:7]


T = int(input())

for test_case in range(1, T+1):
    answer = 0
    K = int(input())

    magnets = [[] for _ in range(5)]
    for i in range(4):
        magnets[i+1] = list(map(int, input().split()))

    revolves = [[] for _ in range(K)]
    for i in range(K):
        revolves[i] = list(map(int, input().split()))

    for revolve in revolves:
        target, direct = revolve
        solution(magnets, target, direct)

    for i in range(1, 5):
        answer += magnets[i][0] * 2 ** (i-1)

    print('#{} {}'.format(test_case, answer))
