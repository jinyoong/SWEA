def Freecell(n, d, g):
    pass
    # 지금까지 한 G판 중 정확히 Pg퍼센트의 판을 이겼다
    # 하지만 반올림을 한 값이 아니므로 지금까지 한 판 G와 0.Pg를 곱하면 정수가 나온다는 뜻이다
    # 마찬가지로 오늘 D판의 게임ㅇ르 해서
    start = 1
    if 100 % d == 0:
        temp = 100 // d
    else:
        temp = 100
    while temp * start <= n:
        new_n = temp * start
        new_d = d * start

    if temp <= n and g != 100:
        return 'Possilbe'
    else:
        return 'Broken'

T = int(input())

for test_case in range(1, T + 1):
    n, d, g = map(int, input().split())
    print(f'#{test_case} {Freecell(n, d, g)}')