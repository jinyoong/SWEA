def solution(number):

    result = ''
    i = 1
    while number:
        temp = 2 ** -i
        if number >= temp:
            result += '1'
            number -= temp
        else:
            result += '0'
        i += 1
        if len(result) == 13:
            return 'overflow'

    return result


T = int(input())

for test_case in range(1, T+1):
    number = float(input())
    print("#{} {}".format(test_case, solution(number)))