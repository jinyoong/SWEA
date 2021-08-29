import sys

sys.stdin = open("input.txt")


def ladder(list_in):
    start_list = []

    # 먼저 시작할 수 있는 지점을 뽑아 놓자
    for start_idx in range(100):
        if list_in[0][start_idx] == 1:
            start_list.append(start_idx)

    # 도착지가 2가 될 때까지 진행한다
    # 이 때 행은 0 인덱스부터, 열은 시작 지점의 인덱스부터 시작하므로
    # 초기 행 값과 초기 열 값을 0 과 start 로 초기화 해 놓는다
    for start in start_list:
        move_low_idx = 0
        move_col_idx = start

        # 99행에 도착지가 있으므로 while 문은 98 인덱스까지 진행한다
        # 현재 행이 98 인덱스보다 작거나 같을 동안 계속한다
        while move_low_idx <= 98:

            # 바로 오른쪽에 1이 있어 방향을 오른쪽으로 전환해야 하는 경우
            # 오른쪽으로 한 번 들어가면 바로 아래에 1이 있는 지점까지 오른쪽으로 이동한다
            # 여기서 가로줄이 세로줄을 관통하는 경우가 없다는 것에 주의하자
            # 바로 오른쪽 열로 이동이 가능하면서 동시에 현재 위치의 바로 오른쪽 열에 1이 있다면
            if (move_col_idx + 1) <= 99 and list_in[move_low_idx][move_col_idx + 1] == 1:
                # 오른쪽으로 갈 수 없거나, 1이 안 나올 때까지 오른쪽으로 이동한다
                # 오른쪽으로 전부 이동한 뒤에는 바로 아래 칸으로 한 칸 내려가자
                while (move_col_idx + 1) <= 99 and list_in[move_low_idx][move_col_idx + 1] == 1:
                    move_col_idx += 1
                move_low_idx += 1

            # 왼쪽으로 가야하는 경우도 위와 마찬가지 방식으로 진행하자
            elif (move_col_idx - 1) >= 0 and list_in[move_low_idx][move_col_idx - 1] == 1:
                while (move_col_idx - 1) >= 0 and list_in[move_low_idx][move_col_idx - 1] == 1:
                    move_col_idx -= 1
                move_low_idx += 1

            # 만약 왼쪽이나 오른쪽으로 갈 수 없는 경우 바로 아래 칸으로 내려가므로
            # mobe_low_idx 에 1을 추가하자
            else:
                # 아래로만 내려가야 하는 경우
                move_low_idx += 1

        # 만약 98번째 행에서 바로 아래로 내려왔더니
        # 해당 위치에 2가 있다면 도착지 이므로
        # 시작점인 start 를 반환하고 함수를 끝낸다
        if list_in[move_low_idx][move_col_idx] == 2:
            return start


for i in range(10):
    T = int(input())
    list_in = [list(map(int, input().split())) for _ in range(100)]
    print("#{} {}".format(T, ladder(list_in)))