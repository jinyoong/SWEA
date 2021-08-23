def bbang(numbers):
    # 가진 돈으로 최대한 많은 빵을 사야 한다
    # 잔돈에 대한 말도 없고, 한 종류만 사도 된다
    # 즉, 제일 싼 빵만 최대한 많이 사면 된다.
    min_price = numbers[0]
    if numbers[0] >= numbers[1]:
        min_price = numbers[1]
    return numbers[2] // min_price

T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    print("#{} {}".format(test_case, bbang(numbers)))
