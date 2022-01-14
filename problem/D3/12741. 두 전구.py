def solution(s1, f1, s2, f2):
    if s1 > s2:
        s1, s2 = s2, s1
        f1, f2 = f2, f1

    if f1 <= s2:
        return 0

    if f2 >= f1 > s2:
        return f1 - s2

    if f1 > f2:
        return f2 - s2


T = int(input())
answer = [0] * (T+1)
for test_case in range(1, T+1):
    times = [0] * 101
    s_1, f_1, s_2, f_2 = map(int, input().split())
    answer[test_case] = solution(s_1, f_1, s_2, f_2)

for i in range(1, T+1):
    print('#{} {}'.format(i, answer[i]))
'''
3
1 3 5 7
0 5 2 4
0 5 1 6
'''