def robot_button(list_in):
    o_location = 1
    b_location = 1
    b_list = []
    o_list = []
    robot = []
    for i in range(1, 2*int(list_in[0])+1, 2):
        robot.append(list_in[i])
        if list_in[i] == 'B':
            b_list.append(int(list_in[i+1]))
        else:
            o_list.append(int(list_in[i+1]))

    r_dict = {"B": b_list, "O": o_list}

    total = 0
    idx = 0
    while b_list or o_list:
        # print(b_list, o_list)
        # print(b_location, o_location)
        # print(total)
        # 두 리스트 모두 빈 리스트가 될 때까지 반복
        # 먼저 B와 O 로봇의 위치가 눌러야 하는 버튼의 위치가 아니라면
        # 두 로봇의 위치를 바꿔준다
        # 여기서 만약 둘 중 하나의 로봇이라도 제 위치에 있으면 조건문에 들어간다.
        if b_list:
            if b_location < b_list[0]:
                b_location += 1
            elif b_location > b_list[0]:
                b_location -= 1
            else:
                # 만약 B 로봇이 가야할 버튼에 도착하게 된다면
                # B 로봇이 가야할 버튼을 하나 없애주고 B 로봇 대신에 PASS의 의미로 T를 넣는다
                # 만약 B 로봇이 가야할 버튼에 B가 올라와 있는데
                # O 로봇 차례라면 그냥 넘어가게 된다.
                if robot[idx] == "B":
                    b_list.pop(0)
                    robot[idx] = 'T'
        else:
            pass
        if o_list:
            if o_location < o_list[0]:
                o_location += 1
            elif o_location > o_list[0]:
                o_location -= 1
            else:
                # 만약 O 로봇이 가야할 버튼에 도착하게 된다면
                # O 로봇이 가야할 버튼을 하나 없애주고 O 로봇 대신에 PASS의 의미로 T를 넣는다
                # 만약 O 로봇이 가야할 버튼에 O가 올라와 있는데
                # B 로봇 차례라면 그냥 넘어가게 된다.
                if robot[idx] == "O":
                    o_list.pop(0)
                    robot[idx] = 'T'
        else:
            pass

        # 여기까지 왔다면 모든 로봇이 버튼을 누르거나, 이동을 완료했으므로
        # 전체 초를 1씩 증가시킨다.
        total += 1
        if robot[idx] == 'T':
            # 만약 지금 움직일 차례의 로봇이 버튼을 눌렀다면
            # 다음 로봇을 판단해야 하므로 idx 를 1 증가시킨다.
            idx += 1
    return total


T = int(input())

for test_case in range(1, T+1):
    robot_list = list(map(str, input().split()))
    print(f'#{test_case} {robot_button(robot_list)}')