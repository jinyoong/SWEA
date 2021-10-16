def solution(n, r):

    # nCr = n-1Cr-1 + n-1Cr 이용해보자
    # nCr = nCn-r => 10C2 == 10C8
    # 10C2 = 9C2 + 9C1
    # 10C2 = 9C1 + 8C1 + 7C1 + 6C1 + 5C1 + 4C1 + 3C1 + 2C1 + 2C0 = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
    if r > n-r:
        r = n-r

    if r == 0:
        return 1

    if r == 1:
        return n

    if n == r + 1:
        return n

    num1 = solution(n-1, r-1)
    num2 = solution(n-1, r)

    return num1 + num2


def solution2(n, r):

    x = [i for i in range(n, n-r, -1)]
    y = [i for i in range(2, r+1)]

    for i in range(len(x)):
        for j in range(len(y)):
            if y[j] == 0:
                continue
            if x[i] % y[j] == 0:
                x[i] //= y[j]
                y[j] = 0
                break

    result = 1

    for num in x:
        result *= num

    return result % 1234567891


maximum = 1000001
d = 1234567891

number = [1] * maximum

# (A * B) % C == ((A % C) * (B % C)) % C 이용하기

for i in range(2, maximum):
    number[i] = (number[i-1] * i) % d  # n! 값을 1234567891 로 나눈 값 구하기


def div(number, di):  # di 거듭제곱 구하기

    if di == 2:
        return (number * number) % d

    if di == 1:
        return number

    num = div(number, di//2)

    if di % 2:  # 만약 2의 5제곱이면 => 2^2 * 2^2 * 2 해주기
        return (num % d * num % d * number) % d

    return (num % d * num % d) % d


def solution3(n, r):

    x = number[n]
    y = number[n-r]
    z = number[r]
    k = (y * z) % d

    k_inverse = div(k, d-2)  # 페르마의 소정리를 이용해 mod 연산의 곱셈 역원 구하기

    # 페르마의 소정리
    # a ** (p-1) = 1 (mod p)
    # a * a ** (p-2) = 1 (mod p)
    # a의 mod p의 역원 = a ** p-2 mod p

    return (x * k_inverse) % d


T = int(input())

for test_case in range(1, T+1):
    N, R = map(int, input().split())
    print('#{} {}'.format(test_case, solution3(N, R)))
