def burger_comb(idx, maximum, score):
    global answer
    # global temp

    if maximum > maximum_calorie:  # 지금까지 칼로리를 더한 값이 제한 칼로리를 넘으면!
        if answer < score - burger[idx-1][0]:  # 가장 최근에 더한 버거 점수를 뺀 값이 현재 점수보다 높은지 확인
            answer = score - burger[idx-1][0]
        return

    if idx == n:  # 마지막 버거까지 확인한 경우
        if answer < score:  # 현재까지 더한 점수가 최고 점수보다 높은지 확인
            answer = score
        return

    for i in range(idx, n):  # 버거의 조합을 만듦
        # temp.append(i)
        burger_comb(i+1, maximum+burger[i][1], score+burger[i][0])  # 현재 고른 버거의 다음부터 탐색하면 되니까 이렇게 재귀
        # temp.pop()

    return answer


T = int(input())

for test_case in range(1, T + 1):
    n, maximum_calorie = map(int, input().split())
    burger = [tuple(map(int, input().split())) for _ in range(n)]
    answer = 0
    # temp = []
    print("#{} {}".format(test_case, burger_comb(0, 0, 0)))
