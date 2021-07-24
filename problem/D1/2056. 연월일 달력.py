T = int(input())

month_day = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30,
             '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}

for test_case in range(1, T+1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    if int(month) >= 1 and int(month) < 13:
        if int(day) <= month_day[month]:
            print(f'#{test_case} {year}/{month}/{day}')
        else:
            print(f'#{test_case} -1')
    else:
        print(f'#{test_case} -1')