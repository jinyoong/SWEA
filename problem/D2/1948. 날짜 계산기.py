def day_cal(list_in):
    month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    start_month = list_in[0]
    finish_month = list_in[2]
    start_day = list_in[1]
    finish_day = list_in[3]
    result = 0
    if start_month == finish_month:
        return finish_day - start_day + 1
    for i in range(start_month, finish_month):
        if i == start_month:
            result += month_day[i] - start_day + 1
        else:
            result += month_day[i]
    result += finish_day
    return result

T = int(input())

for test_case in range(1, T + 1):
    day_list = list(map(int, input().split()))
    print(f'#{test_case} {day_cal(day_list)}')