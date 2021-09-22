def n_queen(can_loc, idx):
    global result

    if idx == n:  # 가장 마지막 행까지 퀸을 놓았을 경우
        result += 1
        return

    for i in range(n):  # idx 행에 퀸을 놓을 수 있는지 확인
        if not can_loc[idx][i]:  # idx 행의 i 열에 퀸을 못 놓는 경우 넘어감
            continue

        temp = [ele[:] for ele in can_loc]  # 앞으로 놓을 수 없는 위치를 표시하기 위해 2차원 배열 복사
        temp[idx][i] = False  # 현재 놓은 위치를 False 로 변경

        for j in range(1, n-idx):  # idx 행 다음부터 퀸이 갈 수 없는 위치를 표시하기 시작
            temp[idx + j][i] = False  # idx 행의 i 열과 같은 열에 있는 곳 표시

            if idx + j < n and i + j < n:  # i 열의 오른쪽 대각선 표시
                temp[idx + j][i + j] = False
            if idx + j < n and 0 <= i - j:  # i 열의 왼쪽 대각선 표시
                temp[idx + j][i - j] = False
        n_queen(temp, idx + 1)  # 표시가 끝났으면 다음 행에서 퀸을 놓기 시작!

    return result


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    can_loc = [[True] * n for _ in range(n)]
    idx = result = 0
    print("#{} {}".format(test_case, n_queen(can_loc, idx)))
