import sys

sys.stdin = open('5550.txt')


def solution(string):
    temp = []
    t_dict = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
    for alpha in string:  # 입력받은 울음소리를 하나씩 접근

        if not temp:
            temp.append(alpha)
            continue

        for i in range(len(temp)):  # 현재 개구리의 울음소리로 저장된 배열의 원소 하나씩 접근

            if t_dict[alpha] == len(temp[i]) % 5:  # 저장된 울음소리 다음에 현재 울음소리가 추가될 수 있으면 추가
                temp[i] += alpha
                break
        else:  # temp 에 추가할 수 있는 울음소리가 하나도 없었던 경우 새로운 개구리의 울음소리로 추가
            if alpha != 'c':  # 추가하는게 c 가 아니라면 -1 반환
                return -1
            temp.append(alpha)

    answer = 0
    for ele in temp:
        if not len(ele) % 5:
            answer += 1
        else:
            answer = -1
            return answer

    return answer


T = int(input())

for test_case in range(1, T+1):
    crying = input()
    print(f'#{test_case} {solution(crying)}')
