def animal(n, k):
    # n 개의 뿔과 k 마리의 동물을 수식으로 나타내면 아래와 같다
    # x + y = k
    # 2x + y = n
    # 2x + k - x = n
    # x = n - k
    # 즉, 유니콘은 2k - n 마리, 트윈혼은 n - k 마리가 된다
    return [2 * k - n, n - k]


T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    print("#{}".format(test_case), *animal(n, k))
