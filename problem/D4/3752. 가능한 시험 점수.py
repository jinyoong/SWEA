def combination(lst, cur_cnt, goal_cnt, idx, result):
    global comb_lst

    if cur_cnt == goal_cnt and result not in comb_lst:
        comb_lst.add(result)
        return

    for i in range(idx, len(lst)):
        combination(lst, cur_cnt+1, goal_cnt, i+1, result+lst[i])


def solution(lst):

    for cnt in range(1, N+1):
        combination(lst, 0, cnt, 0, 0)

    return len(comb_lst) + 1


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    comb_lst = set()
    print('#{} {}'.format(test_case, solution(numbers)))

'''
2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1
'''