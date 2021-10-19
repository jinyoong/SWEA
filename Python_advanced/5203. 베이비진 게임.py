def solution(game):
    p = [[0] * 10 for _ in range(2)]
    cnt = 0
    winner = 0

    for i in range(6):

        cnt += 1
        p[0][game[i*2]] += 1
        p[1][game[i*2+1]] += 1

        if cnt < 3:
            continue

        for k in range(1, 3):

            if 3 in p[k-1]:
                return k

            for j in range(8):
                if p[k-1][j] >= 1 and p[k-1][j+1] >= 1 and p[k-1][j+2] >= 1:
                    return k

    return winner


T = int(input())

for test_case in range(1, T+1):
    game = list(map(int, input().split()))
    print(f'#{test_case} {solution(game)}')
