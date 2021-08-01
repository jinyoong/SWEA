def soinsu(number):
    sosu = [2, 3, 5, 7, 11]
    result = [0, 0, 0, 0, 0]
    start_idx = 0
    while number > 1:
        temp = 0
        while number % sosu[start_idx] == 0:
            number //= sosu[start_idx]
            temp += 1
        result[start_idx] = temp
        start_idx += 1
    return result

T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    print(f'#{test_case}', end = " ")
    print(*soinsu(number))