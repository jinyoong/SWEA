T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    set1 = set(input().split())
    set2 = set(input().split())
    print(f'#{test_case} {len(set1.intersection(set2))}')
