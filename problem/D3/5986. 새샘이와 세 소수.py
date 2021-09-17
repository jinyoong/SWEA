def prime():
    is_prime = [True] * 1000
    for i in range(2, 1000):
        if is_prime[i]:
            for j in range(2*i, 1000, i):
                is_prime[j] = False
    result = []
    for i in range(2, 1000):
        if is_prime[i]:
            result.append(i)
    return result


def sum_of_three_prime(number):
    answer = 0
    for z in range(number, number//3-1, -2):
        if z not in prime:
            continue
        if number - z < 4:
            continue
        if number - z == 4:
            answer += 1
            continue
        for y in range(z, 2, -1):
            x = number - z - y
            if x <= y and x in prime and y in prime:
                answer += 1

    return answer


T = int(input())
prime = prime()
for test_case in range(1, T+1):
    number = int(input())
    print(f'#{test_case} {sum_of_three_prime(number)}')
