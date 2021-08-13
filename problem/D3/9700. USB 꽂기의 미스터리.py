def usb_mustery(p, q):
    """
    :param p: 올바른 면으로 USB를 꽂을 확률
    :param q: 올바른 면으로 시도할 때 꽂히지 않을 확률
    :return: 1번 뒤집어서 성공할 확률이 2번 뒤집어서 성공할 확률보다 클 경우 'yes', 아니면 'no' 반환
    1. 1번 뒤집어서 성공할 확률
    즉, 1번 뒤집어서 성공해야 하는데 결국 이 말은 처음 시도할 경우에는 뒤집어져 있다는 말이 된다.
    처음 꽂으려고 시도할 때 뒤집어서 시도할 확률 : 1 - p
    2번째 시도에 성공할 확률 : q
    결론적으로 s1 = (1-p) * q

    2. 2번 뒤집어서 성공할 확률
    즉, 처음에는 올바른 방향으로 시도했는데 실패, 두 번째는 뒤집힌 방향이므로 실패, 3번째 시도에 성공
    처음 시도시 올바른 방향인데 실패 : p * (1-q)
    두 번째 시도는 무조건 실패 이므로 : 1
    세 번째 시도는 성공 : q
    결론적으로 s2 = p * (1-q) * q
    """
    s1 = (1-p) * q
    s2 = p * (1-q) * q
    if s1 < s2:
        return 'YES'
    else:
        return 'NO'

T = int(input())

for test_case in range(1, T+1):
    p, q = map(float, input().split())
    print("#{} {}".format(test_case, usb_mustery(p, q)))