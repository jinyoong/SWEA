def make_binary(num):  # 4자리 2진수 만들기

    result = ''

    while num > 1:
        x, y = divmod(num, 2)
        result = str(y) + result
        num = x
    result = str(num) + result

    length = len(result)

    return '0'*(4-length) + result


def solution(number):  # 16진수의 각 자리를 4자리 2진수로 만들기

    hexadecimal = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    answer = ''

    for num in number:
        if num in hexadecimal.keys():
            decimal = hexadecimal[num]
        else:
            decimal = int(num)

        answer += make_binary(decimal)

    return answer


T = int(input())

for test_case in range(1, T+1):
    n, number = input().split()
    N = int(n)
    print("#{} {}".format(test_case, solution(number)))
