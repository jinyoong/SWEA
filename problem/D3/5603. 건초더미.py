def move_hays(hays, hays_mean):
    result = 0  # 평균보다 큰 건초더미에서 차이만큼 옮기면 된다
    for hay in hays:
        if hay > hays_mean:
            result += hay - hays_mean
    return int(result)


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    hays_sum = 0
    hays = [0] * n
    for i in range(n):
        hays[i] = int(input())
        hays_sum += hays[i]
    hays_mean = hays_sum / n
    print('#{} {}'.format(test_case, move_hays(hays, hays_mean)))
