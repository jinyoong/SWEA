import sys

sys.stdin = open("input.txt")


def palindrome(n, m, sentences):
    # 가로 방향에 길이가 m 인 회문이 존재하는지 확인하자
    for i in range(n):
        # 가로 방향이므로 모든 행을 탐색해야 하고
        for j in range(n-m+1):
            # 열은 n-m 인덱스까지 탐색을 진행해야 한다.
            # 여기서 j 는 회문이 시작할 시작 인덱스로 사용하기 때문
            garo_temp = sentences[i][j:j+m]
            # 길이가 j 인덱스부터 길이가 m 인 부분을 뽑아보자
            if garo_temp == garo_temp[::-1]:
                # 만약 이 리스트가 회문이면 끝!
                # 문자열로 반환해야 하니가 join 함수를 사용하자
                return ''.join(garo_temp)

    # 세로 방향에 길이가 m 인 회문이 존재하는지 확인하자
    for j in range(n):
        # 세로 방향이므로 모든 열을 탐색해야 하고
        for i in range(n-m+1):
            # 행은 n-m 인덱스까지 탐색
            sero_temp = ''
            for k in range(m):
                # 길이가 m 인 회문을 찾으니까 m 개의 요소를 문자열로 더해주자
                sero_temp += sentences[i+k][j]
            if sero_temp == sero_temp[::-1]:
                return sero_temp


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    sentences = [list(input()) for _ in range(n)]
    print("#{} {}".format(test_case, palindrome(n, m, sentences)))