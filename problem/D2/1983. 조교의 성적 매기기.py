score_list = ['A+', 'A0', 'A-', 'B+', 'B0',
              'B-', 'C+', 'C0', 'C-', 'D0']

def hakjum(list_in, n, k):
    result = 0
    max_ct = 0
    for score in list_in:
        if list_in[k-1] < score:
            max_ct += 1

    hak = (max_ct + 1) / (n // 10)
    for i in range(1, 11):
        if (i-1) < hak <= i:
            result = score_list[i-1]
            break
    return result

T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    test_list = []
    for _ in range(n):
        middle, final, hw = map(int, input().split())
        temp = middle * 0.35 + final * 0.45 + hw * 0.2
        test_list.append(temp)

    print(f'#{test_case} {hakjum(test_list, n, k)}')