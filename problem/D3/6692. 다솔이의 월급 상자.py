def salary(salarys):
    # n 경우가 주어지는데 각 경우 별로의 기댓값을 구해서 더하면 된다
    result = 0
    for sal in salarys:
        result += sal[0] * sal[1]
    return result

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    salarys = [list(map(float, input().split())) for _ in range(N)]
    print("#{} {:.6f}".format(test_case, salary(salarys)))
