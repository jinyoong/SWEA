def omok(n, list_in):
    # 가로줄에 있는지 확인
    result = 'NO'
    for i in range(n):
        stop = True
        for j in range(n-4):
            if list_in[i][j:j+5] == 'ooooo':
                result = 'YES'
                stop = False
                break
        if not stop:
            break
    if result == 'YES':
        # print('가로줄에 있습니다.')
        return result

    # print('세로줄을 봅니다')
    # 세로줄에 있는지 확인
    for i in range(n):
        stop = True
        for j in range(n-4):
            temp = ''
            for k in range(5):
                temp += list_in[j+k][i]
            if temp == 'ooooo':
                result = 'YES'
                stop = False
                break
        if not stop:
            break
    if result == 'YES':
        # print('세로줄에 있습니다.')
        return result

    # print('오른족 아래 대각선을 봅니다')
    # 오른쪽 아래로 내려가는 대각선에 있는지 확인
    for i in range(n-4):
        stop = True
        for j in range(n-4):
            temp = ''
            for k in range(5):
                temp += list_in[i+k][j+k]
            if temp == 'ooooo':
                result = 'YES'
                stop = False
                break
        if not stop:
            break
    if result == 'YES':
        # print('오른쪽 아래 대각선에 있습니다.')
        return result

    # print('왼쪽 아래 대각선을 봅니다')
    # 왼쪽 아래로 내려가는 대각선에 있는지 확인
    for i in range(n-4):
        stop = True
        for j in range(n-4):
            temp = ''
            for k in range(5):
                temp += list_in[i+k][-(j+1)-k]
            if temp == 'ooooo':
                result = 'YES'
                stop = False
                break
        if not stop:
            break
    if result == 'YES':
        # print('왼쪽 아래 대각선에 있습니다.')
        pass
    else:
        # print('오목이 되는 경우가 없습니다.')
        pass

    return result

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    omok_list = []
    for i in range(n):
        temp = input()
        omok_list.append(temp)
    print(f'#{test_case} {omok(n, omok_list)}')