T = int(input())

for test_case in range(1, T+1):
    result = ''
    num1, num2 = map(int, input().split())
    if num1 < num2:
        result = '<'
    elif num1 == num2:
        result = '='
    else:
        result = '>'
    print('#{} {}'.format(test_case, result))