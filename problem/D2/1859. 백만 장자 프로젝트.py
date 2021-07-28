def max_money(list_in, l):
    result = 0
    max_mon = list_in[-1]
    for i in range(-2, -(l+1), -1):
        if max_mon > list_in[i]:
            result += max_mon - list_in[i]
        else:
            max_mon = list_in[i]
    return result

T = int(input())

for test_case in range(1, T+1):
    case_len = int(input())
    case_list = list(map(int, input().split()))
    print(f'#{test_case} {max_money(case_list, case_len)}')