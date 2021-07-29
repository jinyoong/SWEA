def puzzle(list_in, n, k):
    garo_result = 0
    sero_result = 0
    for i in range(n):
        garo_idx = 0
        while garo_idx < n:
            if list_in[i][garo_idx] == 1:
                temp = 0
                while garo_idx < n and list_in[i][garo_idx] == 1 :
                    temp += 1
                    garo_idx += 1
                if temp == k:
                    garo_result += 1
            else:
                garo_idx += 1
    for j in range(n):
        sero_idx = 0
        while sero_idx < n:
            if list_in[sero_idx][j] == 1:
                temp = 0
                while sero_idx < n and list_in[sero_idx][j] == 1:
                    temp += 1
                    sero_idx += 1
                if temp == k:
                    sero_result += 1
            else:
                sero_idx += 1
    return garo_result + sero_result
T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    puzzle_list = []
    for i in range(n):
        temp = list(map(int, input().split()))
        puzzle_list.append(temp)
    print(f'#{test_case} {puzzle(puzzle_list, n, k)}')