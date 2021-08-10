def is_binary_n(number, n):
    binary = ""
    while number > 1:
        x, y = divmod(number, 2)
        number = x
        binary += str(y)
    binary += str(number)
    # 위의 코드는 number를 2진수로 바꿔주는 코드이다
    # 이 때 2진수가 정렬될 때 거꾸로 정렬이 되게 만들었는데
    # 예를 들면 2의 경우 10이지만, 위의 코드로는 01이 된다.
    # 우리는 마지막 n개의 비트가 모두 1인지 확인하면 되므로
    # 2진수가 뒤집어져있던 바로있던 상관이 없다
    if binary[:n] == '1' * n:
        return 'ON'
    else:
        return 'OFF'

T = int(input())

for test_case in range(1, T+1):
    n, number = map(int, input().split())
    print(f'#{test_case} {is_binary_n(number, n)}')