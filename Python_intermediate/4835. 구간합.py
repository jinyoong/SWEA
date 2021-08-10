import sys

sys.stdin = open("input.txt")

def guganhap(n, m, numbers):
    """
    :param n: numbers 리스트의 길이
    :param m: 합을 구해야 하는 구간의 길이
    :param numbers: 정수가 들어있는 리스트
    :return: 가장 큰 구간합과 가장 작은 구간합의 차이를 반환
    n개의 길이를 가지는 numbers 리스트에서 m개식 나누어 더해야 한다
    즉 n = 5, m = 3 이라면 (0, 1, 2), (1, 2, 3), (2, 3, 4) 의 3가지 경우가 나온다
    시작하는 인덱스는 0 ~ 2 인데 이는 0 ~ n-m 까지라고 볼 수 있다.
    따라서 반복문을 해당 횟수만큼 진행하며 시작 인덱스를 정하고
    시작 인덱스부터 m개의 숫자를 더하면 되므로 반복문을 추가한다.
    """
    max_hap = 0
    min_hap = 0
    for i in range(n-m+1):
        # 시작 인덱스를 정하는 반복문
        gugan_hap = 0
        for j in range(i, i+m):
            # 시작 인덱스부터 연속한 m개의 숫자를 모두 더하는 반복문
            gugan_hap += numbers[j]
        if i == 0:
            # 제일 처음 나오는 구간합을 최대, 최소로 지정하자
            min_hap = max_hap = gugan_hap
        else:
            if max_hap < gugan_hap:
                max_hap = gugan_hap
            if min_hap > gugan_hap:
                min_hap = gugan_hap
    return max_hap - min_hap

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    print("#{} {}".format(test_case, guganhap(n, m, numbers)))