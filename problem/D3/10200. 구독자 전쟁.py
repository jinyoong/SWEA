def subscirbe_min_max(n, p, t):
    """
    n 명의 전체 사람 중 p 와 t 의 교집합의 범위를 구하는 문제라고 생각하면 된다.
    우선 교집합의 최댓값은 아주 구하기 쉬운데 p와 t 중 작거나 같은 수가 교집합의 최댓값이 된다.
    교집합의 최솟값을 구하기 위해선 집합에서의 연산을 생각해보면 된다.
    n(n) >= n(p U t) = n(p) + n(t) - n(p ^ t) 이기 때문에
    n(p ^ t) >= n(p) + n(t) - n(n)이 되므로 n(p ^ t) = max(n(p) + n(t) - n(n), 0)이 된다.
    """
    max_num = min(p, t)
    min_num = max(p + t - n, 0)
    return max_num, min_num

T = int(input())

for test_case in range(1, T + 1):
    n, p, t = map(int, input().split())
    result = subscirbe_min_max(n, p, t)
    print(f'#{test_case} {result[0]} {result[1]}')