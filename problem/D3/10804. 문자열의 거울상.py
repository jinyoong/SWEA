def string_mirror(alpha_in):
    alpha_ch_dict = {'p': 'q', 'q': 'p', 'b': 'd', 'd': 'b'}
    result = ''
    for alpha in alpha_in:
        result = alpha_ch_dict[alpha] + result
    return result

T = int(input())

for test_case in range(1, T+1):
    alpha = input()
    print(f'#{test_case} {string_mirror(alpha)}')