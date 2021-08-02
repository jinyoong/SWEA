def sheep(number):
    plus_number = number
    result = 0
    num_set = set()
    multi = 1
    while True:
        result += 1
        temp = set(str(number))
        num_set.update(temp)
        if len(num_set) == 10:
            break
        number += plus_number
    return number

T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    print(f'#{test_case} {sheep(number)}')