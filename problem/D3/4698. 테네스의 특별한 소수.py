def find_prime():
    maximum = 10**6+1
    is_prime = [True] * maximum
    for i in range(2, maximum):
        if is_prime[i]:
            for j in range(2*i, maximum, i):
                is_prime[j] = False
    answer = set()
    for i in range(2, maximum):
        if is_prime[i]:
            answer.add(i)

    return answer


def special_prime(d, a, b):
    result = 0
    for i in range(a, b+1):
        if i in prime and str(d) in str(i):
            result += 1

    return result


prime = find_prime()
T = int(input())
print(prime)
for test_case in range(1, T+1):
    D, A, B = map(int, input().split())
    print(f'{test_case} {special_prime(D, A, B)}')
