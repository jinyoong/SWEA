def couple(string_in):
    alpha_set = set(string_in)
    alpha_dict = {}
    for alpha in list(alpha_set):
        alpha_dict[alpha] = string_in.count(alpha)

    result = []
    for key in alpha_dict:
        if alpha_dict[key] % 2 == 1:
            result.append(key)

    if not result:
        return 'Good'
    else:
        result.sort()
        return ''.join(result)

T = int(input())
for test_case in range(1, T+1):
    alpha = input()
    print(f'#{test_case} {couple(alpha)}')