import sys

sys.stdin = open("input.txt")

def bus(k, n, chargers):
    """
    :param k: 한 번 충전으로 최대한 이동할 수 있는 정류장의 수
    :param n: 종점의 번호. 즉, 0 ~ n 번 정류장이 존재한다
    :param chargers: 충전기가 있는 정류장의 번호 리스트
    :return: 종점까지 가기 위한 최소 충전 횟수
    먼저 버스가 위치하고 있는 현재 지점을 bus_location 이라 하자
    충전기가 아주 적절히 배치되어 있다고 가정한다면, 버스는 매 이동 시 최대 거리 k 만큼 이동하는 것이 효율적이다.
    따라서 먼저 현재 위치 bus_location 에 k 를 더한 값이 chargers 에 있는지 확인하자
    있다면 최대 이동을 하면 되지만 없으면 문제가 생긴다.

    최대 이동한 정류장이 chargers 에 없는 경우
    최소한으로 충전하기 위해서는 갈 수 있는 한 많이 간 뒤 충전하는게 핵심이다.
    따라서 다음 이동은 k-1 만큼, 그래도 없으면 k-2 만큼 이동하는 방식으로 1만큼 이동할 때까지 반복하자
    만약 그 사이에 충전기가 있으면 그 위치로 이동하고 반복문을 종료하고, 1만큼 이동할때까지 충전기가 없다면
    절대 종점에 도착할 수 없으므로 0을 반환하자

    만약 충전을 한 뒤 k 만큼 이동한 결과가 종점 이상까지 이동할 수 있다면
    버스가 안전하게 도착한 것이므로 반복문을 종료하고 결과를 반환한다.
    """
    result = 0
    bus_location = 0
    while bus_location < n:
        # 버스가 아직 종점에 도착하지 않은 상태
        if bus_location + k in chargers:
            # 버스가 최대 이동을 했을 때 충전기가 있다면
            # 최대한 이동한 뒤 충전한다.
            bus_location += k
            result += 1

        else:
            # 만약 버스가 최대 이동을 했는데 충전기가 없다면
            # 먼저 크게 2가지로 나뉜다.
            # 버스가 종점 이상으로 이동할 수 있거나 그 전 충전기에서 충전해야 한다

            if bus_location + k >= n:
                # 버스가 종점 이상으로 이동할 수 있는 경우
                break

            for i in range(k-1, 0, -1):
                # 버스가 최대거리보다 적게 가야 충전기를 만날 수 있는 경우
                if bus_location + i in chargers:
                    bus_location += i
                    result += 1
                    break
            else:
                # 버스가 이동할 수 있는 경로에 충전기가 없는 경우
                # 더 이상 종점에 갈 수 없으므로 0을 반환
                return 0

    return result


T = int(input())

for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    chargers = list(map(int, input().split()))
    print("#{} {}".format(test_case, bus(k, n, chargers)))