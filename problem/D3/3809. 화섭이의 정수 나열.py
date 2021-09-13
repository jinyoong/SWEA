def digit_sort(numbers):
    number = 0
    while True:
        if str(number) not in numbers:
            return number
        number += 1


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    numbers = ''
    while len(numbers) != n:
        num_lst = list(input().split(" "))
        numbers += ''.join(num_lst)
    print(f'#{test_case} {digit_sort(numbers)}')
