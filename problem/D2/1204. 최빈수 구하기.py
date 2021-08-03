def mode(numbers):
    new_numbers = list(set(numbers))
    result = []
    for number in new_numbers:
        result.append([number, numbers.count(number)])
    result = sorted(result, key=lambda x: (x[1], x[0]), reverse=True)
    return result

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{test_case} {mode(numbers)[0][0]}')