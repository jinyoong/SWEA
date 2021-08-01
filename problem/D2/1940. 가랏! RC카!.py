def rc_drive(list_in):
    result = 0
    velocity = 0
    for element in list_in:
        if element[0] == 0:
            pass
        elif element[0] == 1:
            velocity += element[1]
        else:
            if velocity >= element[1]:
                velocity -= element[1]
            else:
                velocity = 0
        result += velocity
    return result

T = int(input())

for test_case in range(1, T+1):
    command = int(input())
    rc_list = []
    for i in range(command):
        temp = list(map(int, input().split()))
        rc_list.append(temp)
    print(f'#{test_case} {rc_drive(rc_list)}')