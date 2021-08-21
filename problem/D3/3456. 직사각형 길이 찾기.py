def find_side(numbers):
    square_dict = {}  # 변의 길이와 개수를 담을 딕셔너리
    for number in numbers:
        # 딕셔너리에 변의 길이가 몇 개 주어졌는지 집어넣자
        square_dict[number] = square_dict.get(number, 0) + 1
    # 변의 개수가 홀수개인 변의 길이를 추가해주면 직사각형이 된다
    for key, value in square_dict.items():
        if value % 2:
            return key


T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    print("#{} {}".format(test_case, find_side(numbers)))
