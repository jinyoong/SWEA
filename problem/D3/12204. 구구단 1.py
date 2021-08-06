def isgugu(number):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(1, 10):
        if number % i == 0 and number // i in num_list:
            result = 'Yes'
            break
    else:
        result = 'No'
    return result


T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    print(f'#{test_case} {isgugu(number)}')