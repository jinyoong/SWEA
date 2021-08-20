def harvesting(n, farm):
    """
    농장의 크기가 n(홀수) 이면 시작하는 곳은 n // 2  + 1이 된다
    이 곳 내에서 마름모 형태로 수확을 진행하는데
    점차 증가하다가 n // 2 열에서 모든 행을 전부 수확한 뒤 다시 감소한다
    농장의 크기가 5 라면 가정하게 되면
    0열 : 2 행 / 1열 : 1 ~ 3 행 / 2열 : 0 ~ 4행 / 3열 : 1 ~ 3행 / 4열 : 2행 순으로 진행이 된다
    """
    col = n // 2
    result = 0
    # 수확은 이차원 배열에서 위치가 [col][0] 인 곳에서 [col][n-1] 에서 끝나게 된다
    for idx in range(n):
        # 행은 n // 2 열에서 전부 선택했다가 그 이후부터는 줄어든다
        new_idx = idx
        if idx > n // 2:
            # 만약 현재 열이 n//2 열보다 큰 열이라면
            # 다시 수확하는 범위가 줄어야 한다
            new_idx = n - idx - 1

        # 수확은 가운데 행을 기준으로 각각 new_idx 만큼을 더 수확하게 된다
        for low in range(col - new_idx, col + new_idx + 1):
            result += farm[low][idx]
    return result


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    print("#{} {}".format(test_case, harvesting(n, farm)))
