def shipship(ship):
    result = 0
    funny_day = []
    for day in ship[1:]:
        if not funny_day:  # 항구에 방문한 배가 없으면 바로 추가
            result += 1
            funny_day.append([day-1, 1])  # 항구에 올 때까지 걸린 날과 방문 횟수를 저장
            continue

        not_visited = True  # 한 번도 방문한 적 없는 배인지 확인하기 위한 변수
        for fun in funny_day:  # 지금까지 방문한 배들의 간격과 횟수를 가지고 판단
            if (day-1) == fun[0] * (fun[1] + 1):  # 방문했던 배가 온 경우
                fun[1] += 1  # 해당 배가 방문한 횟수를 1 증가
                not_visited = False  # 새로운 배가 아니므로 False 로 저장

        if not_visited:  # 만약 한 번도 방문하지 않은 배라면
            funny_day.append([day-1, 1])  # 방문 간격과 횟수를 추가
            result += 1

    return result


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    ship = [int(input()) for _ in range(n)]
    print('#{} {}'.format(test_case, shipship(ship)))
