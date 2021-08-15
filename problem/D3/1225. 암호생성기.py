def password(numbers):
    subtract = [1, 2, 3, 4, 5]
    idx = 0
    while numbers[0] - subtract[idx] > 0:
        numbers[0] -= subtract[idx]
        numbers.append(numbers.pop(0))
        idx += 1
        idx %= 5
    numbers.pop(0)
    numbers.append(0)
    return numbers

for _ in range(10):
    test_case = int(input())
    numbers = list(map(int, input().split()))
    print(f"#{test_case}", end=" ")
    print(*password(numbers))