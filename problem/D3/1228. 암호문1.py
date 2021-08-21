def password(origin_password, command_ct, command_list):
    insert_list = [[]] * command_ct
    start_idx = 1
    command_list.append('I')
    ct = 0
    for i in range(1, len(command_list)):  # I 와 같이 들어온 x, y, s 를 구분하자
        if command_list[i] == 'I':
            insert_list[ct] = command_list[start_idx:i]  # start_idx 에서 I 전까지가 x, y, s 에 해당
            start_idx = i + 1  # 다음 start_idx 는 I 의 바로 다음!
            ct += 1

    for command in insert_list:  # x, y, s 를 규칙에 맞게 넣어주자
        insert_ct = int(command[1])
        insert_idx = int(command[0])
        for j in range(insert_ct):
            origin_password.insert(insert_idx+j, command[2+j])
            # 1, 3, 10, 11, 12 으로 주어졌다고 하자
            # 반복문 순서에 의해서 10, 11, 12 순으로 추가가 되는데
            # 계속해서 1 번 인덱스에 추가하면 결과는 12, 11, 10 으로 위치하게 된다
            # 따라서 추가하는 인덱스도 하나씩 늘려가자
    return origin_password[:10]


for test_case in range(1, 11):
    origin_len = int(input())
    origin_password = list(map(int, input().split()))
    command_ct = int(input())
    command_list = input().split()
    print("#{}".format(test_case), *password(origin_password, command_ct, command_list))
