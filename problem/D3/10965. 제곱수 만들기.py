# prime2_list = [2]
# for i in range(3, 5000000):
#     # print(f'{i}가 소수인지 판단합니다.')
#     for j in range(2, round(i ** 0.5) + 1):
#         # print(f'{i}를 {j}로 나눠봅니다.')
#         if i % j == 0:
#             break
#     else:
#         prime2_list.append(i)
#
# print(prime2_list)

max_n = int((10 ** 7) ** 0.5)
test_prime = [False, False] + [True] * (max_n-1)
prime_list = []

for i in range(2, max_n+1):
    if test_prime[i]:
        prime_list.append(i)
        for j in range(2*i, max_n+1, i):
            test_prime[j] = False

def gobgob(number):
    idx = 0
    if number == 1:
        return 1
    else:
        result = 1
        while number != 1 and idx < len(prime_list):
            if number % prime_list[idx] == 0:
                # print(f'{number}가 {prime_list[idx]}로 나뉩니다.')
                ct = 0
                while number % prime_list[idx] == 0:
                    ct += 1
                    number //= prime_list[idx]
                if ct % 2:
                    result *= prime_list[idx]
            idx += 1
        if number != 1:
            result *= number
    return result


T = int(input())
answer = []
for test_case in range(1, T+1):
    number = int(input())
    answer.append(f'#{test_case} {gobgob(number)}')
for ans in answer:
    print(ans)