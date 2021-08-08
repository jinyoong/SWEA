def dart(point_list):
    score = 0
    for point in point_list:
        distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
        if distance % 20 == 0:
            score += int(11 - (distance // 20))
        else:
            distance_pt = (distance // 20) + 1
            score += 11 - distance_pt
    return int(score)

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    point_list = []
    for i in range(n):
        temp = list(map(int, input().split()))
        point_list.append(temp)
    print(f'#{test_case} {dart(point_list)}')