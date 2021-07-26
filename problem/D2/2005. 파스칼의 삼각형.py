def pascal(number, list_in):
    if number <= 2:
        return [1] * number
    else:
        result = [1] * number
        for i in range(1, number - 1):
            result[i] = list_in[i] + list_in[i-1]
        return result

N = int(input())

answer = []
for test_case in range(1, N + 1):
    case_num = int(input())
    print(f'#{test_case}')
    for num in range(1, case_num + 1):
        answer = pascal(num, answer)
        print(*answer)