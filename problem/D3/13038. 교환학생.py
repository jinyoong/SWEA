def find_days(n, days, temp):
    answer = 0
    week, day = divmod(n, days)

    if day == 0:  # 나누어 떨어지면 마지막 주에는 마지막 강의가 개설된 날짜를 더해주면 된다
        answer += (week - 1) * 7
        day = days
    else:
        answer += week * 7

    min_days = 7
    for i in range(7):
        if not temp[i]:
            continue

        plus = 1
        cnt = 1
        while cnt != day:
            idx = (i + plus) % 7
            # print('시작부터 지난 날: {}, 현재 인덱스: {}, 수업 들은 횟수: {}, 강의실 존재: {}'.format(plus, idx, cnt, temp[idx]))
            plus += 1
            if temp[idx]:
               cnt += 1

        if plus < min_days:
            min_days = plus

    return answer + min_days


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    temp = list(map(int, input().split()))
    days = temp.count(1)

    print('#{} {}'.format(test_case, find_days(n, days, temp)))

'''
3
2
0 1 0 0 0 0 0
100000
1 0 0 0 1 0 1
1
1 0 0 0 0 0 0

2
2
0 1 0 0 0 1 0
6
0 1 0 0 0 1 0
답 : 4, 18
오답 : 5, 19
'''
