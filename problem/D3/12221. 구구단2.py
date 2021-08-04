def gugudan(num1, num2):
    if num1 > 9 or num2 > 9:
        return -1
    else:
        return num1 * num2

T = int(input())

for test_case in range(1, T+1):
    x, y = map(int, input().split())
    print(f'#{test_case} {gugudan(x, y)}')