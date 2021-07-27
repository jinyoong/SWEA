def middle_avarge(list_in):
    max_num = list_in[0]
    min_num = list_in[0]
    result = 0
    for element in list_in:
        if max_num < element:
            max_num = element
        if min_num > element:
            min_num = element
        result += element
    result -= (max_num + min_num)
    return round(result/(len(list_in)-2))

T = int(input())

for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    print(f'#{test_case} {middle_avarge(num_list)}')