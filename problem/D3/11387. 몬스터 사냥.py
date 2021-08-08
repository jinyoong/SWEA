def hunt(d, l, n):
    result = 0
    for i in range(n):
        result += d * (100 + (i * l)) // 100
    return result

T = int(input())

for test_case in range(1, T+1):
    d, l, n = map(int, input().split())
    print(f'#{test_case} {hunt(d, l, n)}')