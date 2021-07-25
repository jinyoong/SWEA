num1, num2 = map(int, input().split())

score = [3, 1, 2, 3, 1]

if score[num1 - 1] == num2:
    print('A')
elif score[num1 + 1] == num2:
    print('B')


