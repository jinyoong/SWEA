def revolve(list_in, N):
    # 90도 회전하기
    # 2차원 배열에서 1번째 요소를 위로 읽으면 된다
    result = []
    for i in range(N):
        result.append([0] * 3)
        temp = ''
        for j in range(-1, -(N + 1), -1):
            temp += str(list_in[j][i])
        result[i][0] = temp

    # 180도 회전하기
    # 2차원 배열에서 1번째 요소들의 각 값들을 거꾸로 읽되, 1번째 요소를 읽는 순서도 반대
    for i in range(-1, -(N + 1), -1):
        temp = ''
        for j in range(-1, -(N + 1), -1):
            temp += str(list_in[i][j])
        result[-i-1][1] = temp

    # 270도 회전하기
    for i in range(-1, -(N + 1), -1):
        temp = ''
        for j in range(N):
            temp += str(list_in[j][i])
        result[-i-1][2] = temp
    return result

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_list = []
    for i in range(N):
        temp = list(map(int, input().split()))
        num_list.append(temp)
    print(f'#{test_case}')
    for i in range(N):
        print(*revolve(num_list, N)[i])