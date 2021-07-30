def ssort(list_in, N):
    for _ in range(N):
        for i in range(N-1):
            if list_in[i] > list_in[i+1]:
                list_in[i], list_in[i+1] = list_in[i+1], list_in[i]
    return list_in

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    print(f'#{test_case}', end=' ')
    print(*ssort(num_list, N))