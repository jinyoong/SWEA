T = int(input())

for i in range(1, T+1):
    num_list = list(map(int, input().split()))
    max_num = num_list[0]
    for num in num_list:
        if max_num < num:
            max_num = num
    print('#{} {}'.format(i, max_num))