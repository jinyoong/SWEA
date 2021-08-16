import sys

sys.stdin = open("input.txt")


def bus_stop(bus_list, stop_list):

    # 정류장의 번호는 1 ~ 5000 이므로 0 리스트를 만든 뒤에
    # 해당 정류장을 지나가는 노선이 있을 때마다 1씩 증가시켜 주자!
    bus_line = [0] * 5001

    # 입력되는 순서대로
    # i 번 노선이 지나가는 정류장의 시작 번호, 끝 번호가 된다
    # 매 반복마다 시작 번호부터 끝 번호 까지를 1 증가시켜주자
    # 즉 1번 노선의 버스가 1번 정류장부터 3번 정류장을 지나게 되면
    # bus_line 에서 1번 인덱스 부터 3번 인덱스 까지의 값이 1 증가하게 된다
    for bus in bus_list:
        start_num = bus[0]
        end_num = bus[1]
        for i in range(start_num, end_num + 1):
            bus_line[i] += 1

    # 각 정류장을 지나가는 노선들의 개수를 알았으므로
    # 문제에서 요구하는 정류장을 지나는 노선들을 차례대로 출력하면 된다
    result = []

    for pick in stop_list:
        result.append(bus_line[pick])

    return result

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    bus_list = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    stop_list = [int(input()) for _ in range(p)]
    print("#{}".format(test_case), *bus_stop(bus_list, stop_list))
