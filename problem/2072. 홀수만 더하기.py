T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    list_in = list(map(int, input().split()))
    total = 0
    for ele in list_in:
        if ele % 2:
            total += ele
    print('#{} {}'.format(test_case, total))