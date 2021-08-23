def days(numbers):
    day = [0, 1, 2, 3, 4, 5, 6]  # 월 ~ 일 까지의 숫자 리스트
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 각 월의 날짜를 담은 리스트
    accumulate_month = [0] * 13  # 해당 월까지의 누적 날짜 수
    for i in range(1, 13):
        accumulate_month[i] = month[i] + accumulate_month[i-1]
    idx = (accumulate_month[numbers[0]-1] + numbers[1] + 3) % 7  # 1월 1일이 금요일(4) 였으므로 +3 을 해주자
    return day[idx]


T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    print("#{} {}".format(test_case, days(numbers)))
