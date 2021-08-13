def snack_distribution(snack, people):
    """
    :param snack: 입력받는 과자의 개수
    :param people: 입력받는 인원의 수
    :return: 과자를 최대한 균등하게 분배할 시 나오는 최대값과 최소값의 차이
    우선 과자를 쪼갤 수 없으면서 균등하게 나눠야 하므로 몫과 나머지를 이용하자
    sncak % people 의 값이 0인 경우 모두에게 똑같은 양을 나눠줄 수 있는 것이고
    sncak % people 이 0이 아니라면 남은 개수를 아무에게나 1개씩 추가로 분배하면 된다.
    즉, 반환되는 값은 0 혹은 1이 된다.
    """
    result = snack % people
    if result == 0:
        return 0
    else:
        return 1

T = int(input())

for test_case in range(1, T+1):
    x, y = map(int, input().split())
    print("#{} {}".format(test_case, snack_distribution(x, y)))
