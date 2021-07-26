def pari(list_in, garo, madi):
    max_kill = 0
    for i in range(garo-madi+1):
        for j in range(garo-madi+1):
            kill_ct = 0
            for k in range(madi):
                kill_ct += sum(list_in[i+k][j:j+madi])
                if max_kill < kill_ct:
                    max_kill = kill_ct
    return max_kill

T = int(input())

for test_case in range(1, T+1):
    garo, madi = map(int, input().split())
    pari_list = []
    for i in range(garo):
        temp = list(map(int, input().split()))
        pari_list.append(temp)

    print(f'#{test_case} {pari(pari_list, garo, madi)}')
