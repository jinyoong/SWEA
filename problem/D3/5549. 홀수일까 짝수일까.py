def odd_even(number):
    if int(number[-1]) % 2:
        return 'Odd'
    else:
        return 'Even'


T = int(input())

for test_case in range(1, T + 1):
    number = input()
    print("#{} {}".format(test_case, odd_even(number)))
