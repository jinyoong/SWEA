def normal_number(numbers):
    result = 0
    for i in range(1, len(numbers)-1):
        if numbers[i-1] < numbers[i] < numbers[i+1] or numbers[i+1] < numbers[i] < numbers[i-1]:
            result += 1
    return result

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{test_case} {normal_number(numbers)}')