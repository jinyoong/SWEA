def sdoku(list_in):
    # 먼저 가로줄을 전부 확인하자

    for i in range(9):
        garo_result = [0] * 9
        for j in range(9):
            if list_in[i][j] not in garo_result:
                garo_result[j] = list_in[i][j]
            else:
                return 0

    # 세로줄 확인하자
    for i in range(9):
        sero_result = [0] * 9
        for j in range(9):
            if list_in[j][i] not in sero_result:
                sero_result[j] = list_in[j][i]
            else:
                return 0

    # 구역을 확인하자
    for i in range(0, 9, 3):
        # 먼저 행을 3구역으로 나누자 0 ~ 2, 3 ~ 5, 6 ~ 8 행 순으로 살핀다
        for n in range(3):
            # 3구역으로 나눈 행에서 각 구역당 네모가 3개씩 생긴다
            # 따라서 각 구역의 존재하는 3개의 네모를 다 반복해야 하므로
            # 3번 반복하는 반복문을 추가한다
            area_result = []
            # 각 네모가 조건을 만족하는지 확인해야 하므로 여기에 area_result를 초기화 해준다
            for k in range(i, i+3):
                # 0 ~ 2 행에 있는 3개의 네모는 모두 0행부터 2행까지 봐야 하므로 구간을 i를 이용해 지정한다
                for j in range(3*n , 3+3*n):
                    # 3개의 네모의 열은 0 ~ 2, 3 ~ 5, 6 ~ 8 순으로 증가해야 한다
                    # 따라서 위처럼 반복문을 지정해주자
                    if list_in[k][j] not in area_result:
                        area_result.append(list_in[k][j])
                    else:
                        return 0

    return 1

T = int(input())

for test_case in range(1, T+1):
    sdoku_list = []
    for i in range(9):
        sdoku_ele = list(map(int, input().split()))
        sdoku_list.append(sdoku_ele)
    print(f'#{test_case} {sdoku(sdoku_list)}')