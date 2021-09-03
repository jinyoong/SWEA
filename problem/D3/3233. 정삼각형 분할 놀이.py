def triangle(number):
    result = 0
    for i in range(number):
        result += i * 2 + 1
    return result


T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    number = a // b
    print('#{} {}'.format(test_case, triangle(number)))
