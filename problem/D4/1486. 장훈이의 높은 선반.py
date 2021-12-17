# B 이상인 최소치를 만들어내는 문제
# 탐욕 알고리즘...? 완전 탐색....?


def solution(heights, idx, B, temp):  # 구할 수 있는 모든 조합을 구하자
    global answer
    global stop

    if stop:  # 재귀 함수를 모두 종료
        return

    if idx == N:
        if temp == B:  # 만약 점원들의 합이 딱 선반과 같은 경우
            stop = True  # 이게 답이 된다
            answer = temp

        elif B < temp < answer:  # 합이 선반보다는 크고 지금까지의 최소값보다 작은 경우
            answer = temp  # 초기화

        return

    solution(heights, idx+1, B, temp+heights[idx])
    solution(heights, idx+1, B, temp)


T = int(input())

for test_case in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    answer = N * 10000
    temp = 0
    stop = False
    solution(heights, 0, B, temp)
    print(f'#{test_case} {answer-B}')
