def password2(pw, commands):
    idx = 0
    while idx < len(commands):
        if commands[idx] == 'I':  # 추가해야 하는 경우
            insert_ct = int(commands[idx+2])  # 추가해야 하는 숫자의 개수
            insert_pt = int(commands[idx+1])  # 추가해야 하는 위치
            for i in range(insert_ct):
                pw.insert(insert_pt+i, commands[idx+3+i])  # 숫자를 앞에서부터 추가하면 위치도 1씩 증가
            idx += 3 + insert_ct
        elif commands[idx] == 'D':  # 삭제해야 하는 경우
            delete_ct = int(commands[idx + 2])  # 삭제해야 하는 숫자의 개수
            delete_pt = int(commands[idx + 1])  # 삭제해야 하는 숫자의 위치
            for i in range(delete_ct):
                pw.pop(delete_pt)
            idx += 3

    return pw[:10]


for test_case in range(1, 11):
    n = int(input())
    pw = list(input().split())
    command_ct = int(input())
    commands = list(input().split())
    print("#{}".format(test_case), *password2(pw, commands))
