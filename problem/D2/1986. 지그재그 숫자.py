def zigzag(number):
    result = 0
    for i in range(1, number+1):
        if i % 2:
            result += i
        else:
            result -= i
    return result

T = int(input())

for test_case in range(1, T+1):
    num = int(input())
    print(f'#{test_case} {zigzag(num)}')