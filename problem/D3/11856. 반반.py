def banban(string_in):
    alpha_list = list(set(string_in))
    if len(alpha_list) != 2:
        result = 'No'
    else:
        for alpha in alpha_list:
            if string_in.count(alpha) != 2:
                result = 'No'
                break
        else:
            result = 'Yes'
    return result

T = int(input())

for test_case in range(1, T+1):
    alpha = input()
    print(f'#{test_case} {banban(alpha)}')