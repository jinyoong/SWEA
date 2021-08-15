import sys

sys.stdin = open("input.txt")

def palindrome(numbers):
    # 가로 회문을 보자
    # 가로 회문을 살필 때는 아래와 같은 순서로 진행한다
    # i 행의 j 열부터 시작하는 가로줄을 본다
    # 가로줄의 끝은 99 번 인덱스부터 1 씩 감소한다
    # 만약 i 행의 j 열부터 k 열까지의 리스트가 회문이면
    # i 행의 j 열에서 시작하는 회문은 더 볼 필요가 없으므로 break
    # 만약 j 열에서 99 열까지의 리스트 길이보다 현재 나온 회문의 길이가 더 길면
    # j 이후로는 볼 필요가 없으므로 break
    garo_result = 0
    for i in range(99):
        for j in range(99):
            for k in range(100, j, -1):
                a = numbers[i][j:k]
                b = a[::-1]
                if a == b:
                    if garo_result < len(a):
                        garo_result = len(a)
                    break
            if garo_result >= 100 - j:
                break

    # 세로 회문도 가로 회문과 마찬가지 방식으로 진행한다
    # 단, 세로는 리스트 형식으로 출력할 수 없기 때문에
    # temp 문자열을 초기화 하여 직접 문자열을 만든 뒤 같은 작업을 진행하자
    sero_result = 0
    for j in range(99):
        for i in range(99):
            for k in range(100, i, -1):
                temp = ''
                for l in range(i, k):
                    temp += numbers[l][j]
                if temp == temp[::-1]:
                    if sero_result < len(temp):
                        sero_result = len(temp)
                    break
            if sero_result >= 100 - i:
                break

    if sero_result < garo_result :
        return garo_result
    else:
        return sero_result

for test_case in range(1, 11):
    n = int(input())
    numbers = [list(input()) for _ in range(100)]
    print("#{} {}".format(test_case, palindrome(numbers)))