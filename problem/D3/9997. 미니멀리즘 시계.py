def mini_clock(degree):
    """
    :param degree: 시침이 12를 기준으로 몇 도 기울어져 있는지
    :return: 시와 분을 반환한다.
    먼저 12만 적혀있는 시계로 0시 ~ 11시 까지 모두 표현해야 한다.
    즉, 시계의 구역을 12개로 나누어 각 시간은 30도의 크기를 가진다는 것
    예를 들어 12를 기준으로 20도 기울어진 경우, 첫 30도 안에 들어오므로 0시이며
    30도 안에서 60분을 표현해야 하므로 1도는 2분을 의미하게 된다
    따라서 0시 40분이 되는 것

    결론적으로 주어진 degree를 30으로 나누었을 때의 몫이 시
    degree를 30으로 나눈 나머지에 2를 곱한 값이 분이 된다.
    """
    return degree // 30, degree % 30 * 2

T = int(input())

for test_case in range(1, T+1):
    degree = int(input())
    print("#{} {} {}".format(test_case, mini_clock(degree)[0], mini_clock(degree)[1]))