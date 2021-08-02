def throw_stone(list_in):
    distance_list = []
    min_distance = 100000
    for element in list_in:
        temp = abs(element - 0)
        if temp < min_distance:
            min_distance = temp
        distance_list.append(temp)
    return min_distance, distance_list.count(min_distance)

T = int(input())

for test_case in range(1, T+1):
    case_len = int(input())
    stone_list = list(map(int, input().split()))
    print(f'#{test_case}', end=" ")
    print(*throw_stone(stone_list))
