def magnetic(table_list):
    # 결국 한 열을 위에서부터 내렸을 때, N 극과 S 극이 한 쌍 존재할 때
    # 교착 상태가 1개씩 늘어난다
    # 주의해야 하는 것은 N 극과 S 극이 한 쌍 존재하더라도 순서가 S => N 이면 교착 상태가 되지 않는다
    result = 0
    for j in range(100):
        n_ct = 0
        ans = 0
        # j 열의 모든 행을 차례로 살펴보자
        for i in range(100):

            # 만약 위에서부터 진행하면서 N 극인 1 이 나온다면 N 극의 개수를 1개 늘린다
            if table_list[i][j] == 1:
                n_ct = 1

            # S 극인 2 가 나왔을 때 N 극도 나와 있는 상태라면 둘은 하나로 붙어 교착 상태를 형성한다
            elif table_list[i][j] == 2 and n_ct >= 1:
                ans += 1
                n_ct -= 1
        result += ans
    return result


for test_case in range(1, 11):
    n = int(input())
    table_list = [list(map(int, input().split())) for _ in range(n)]
    print("#{} {}".format(test_case, magnetic(table_list)))
