def time(h1, h2):
    return (h1 + h2) % 24


T = int(input())

for test_case in range(1, T + 1):
    h1, h2 = map(int, input().split())
    print('#{} {}'.format(test_case, time(h1, h2)))
