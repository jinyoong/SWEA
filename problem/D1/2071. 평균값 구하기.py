T = int(input())

for test_case in range(1, T+1):
    list_in = list(map(int, input().split()))
    print('#{} {:.0f}'.format(test_case, sum(list_in)/len(list_in)))