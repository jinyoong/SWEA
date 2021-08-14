def exercise(L, U, X):
    """
    :param L: 최소로 해야 하는 운동 시간
    :param U: 최대로 할 수 있는 운동 시간
    :param X: 해당 주 동안 한 운동의 총 시간
    :return: X 가 U 를 초과하면 -1을, L 보다 작다면 얼마나 더 운동을 해야 하는지 반환
    """
    if X > U:
        return -1
    elif X < L:
        return L - X
    else:
        return 0


T = int(input())

for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    print("#{} {}".format(test_case, exercise(L, U, X)))