def padovan():
    numbers = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90
    for i in range(10, 101):
        numbers[i] = numbers[i-1] + numbers[i-5]
    return numbers


numbers = padovan()
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    print('#{} {}'.format(test_case, numbers[n]))
