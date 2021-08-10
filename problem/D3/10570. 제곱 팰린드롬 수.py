def palindrome(n, m):
    """
    n부터 m 사이의 숫자 x에 대해서 x와 루트 x 모두 양의 정수이면서 회문인 경우
    조건을 만족하게 된다. 따라서 우리는 제곱근이 정수인 경우를 먼저 살펴야 한다
    따라서 n의 제곱근보다 크거나 같은 가장 가까운 정수가 제일 작은 정수 제곱근이고
    제일 큰 정수 제곱근은 int(m ** 0.5)임을 알 수 있다.
    따라서 먼저 제곱근들을 나열한 뒤, 이 중 회문인 경우를 살피고 제곱한 결과가 회문인지 살펴보자
    """
    min_num = int(n ** 0.5)
    if n ** 0.5 % 1:
        min_num += 1
    max_num = int(m ** 0.5)
    result = 0
    for num in range(min_num, max_num + 1):
        if str(num) == str(num)[::-1]:
            if str(num ** 2) == str(num ** 2)[::-1]:
                result += 1
    return result


T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    print(f'#{test_case} {palindrome(n, m)}')