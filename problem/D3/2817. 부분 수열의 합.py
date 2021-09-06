def sum_k(numbers, ct, idx, permu_sum):
    global result

    if permu_sum == k:  # 합이 k 면 중지!
        result += 1
        return

    if ct == n:  # 주어진 수를 모두 골랐는데 k 가 아니면 중지
        return

    if permu_sum > k:  # 중간에 k 보다 커지면 중지
        return

    for i in range(idx, n):  # i 번째 수를 고르면, 다음에는 i+1 번째 숫자부터 본다 => 순열이 아니라 조합!
        if not used[i]:
            used[i] = True
            sum_k(numbers, ct+1, i+1, permu_sum+numbers[i])
            used[i] = False

    return


T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    used = [False] * n
    result = 0
    sum_k(numbers, 0, 0, 0)
    print('#{} {}'.format(test_case, result))
