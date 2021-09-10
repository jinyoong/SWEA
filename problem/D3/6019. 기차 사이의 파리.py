def time(d, a, b, f):
    result = d / (a+b) * f
    return result


T = int(input())

for test_case in range(1, T + 1):
    distance, a, b, fly = map(float, input().split())
    print('#{} {}'.format(test_case, time(distance, a, b, fly)))
