def dalpengi(number):
    result = []
    for i in range(number):
        result.append([0] * number)
    move = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
    garo, sero = 0, 0
    start = 0
    result[garo][sero] = 1
    num = 2
    while num  <= number ** 2:
        try:
            if (garo + move[start][0] < 0 or sero + move[start][1] < 0) \
                    or result[garo + move[start][0]][sero + move[start][1]] != 0:
                start += 1
            start %= 4
            temp = result[garo + move[start][0]][sero + move[start][1]]
        except IndexError:
            start += 1
        else:
            garo += move[start][0]
            sero += move[start][1]
            result[garo][sero] = num
            num += 1
    return result

T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    print(f'#{test_case}')
    for element in dalpengi(number):
        print(*element)