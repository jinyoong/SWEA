def time_sum(time):
    minute_sum = time[1] + time[3]
    hour, minute = divmod(minute_sum, 60)
    hour_sum = (hour + time[0] + time[2])
    if hour_sum % 12 == 0:
        hour_sum = 12
    else:
        hour_sum %= 12
    return hour_sum, minute

T = int(input())

for test_case in range(1, T+1):
    time = list(map(int, input().split()))
    print(f'#{test_case} {time_sum(time)[0]} {time_sum(time)[1]}')