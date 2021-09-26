def max_inc_per(idx, numbers, length, max_num):
    global max_length

    if idx == n:
        if length > max_length:  # 맨 끝 숫자까지 봤을 때 최대 길이 갱신
            max_length = length
        return

    for i in range(idx, n):
        if numbers[i] < max_num:  # 현재 숫자가 전 숫자보다 작을 경우 넘어감
            continue

        if max_length >= length + n-i:  # 현재까지의 길이와 남은 숫자들을 전부 더해도 최대 길이 이상으로 나오지 않으면 돌아감
            return
        # 여기까지 오게 되면 현재 숫자가 다음에 올 수 있는 것
        max_inc_per(i+1, numbers, length+1, numbers[i])  # 현재 숫자를 추가하고 진행
        max_inc_per(i+1, numbers, length, max_num)  # 현재 숫자를 넘어가고 진행


def max_inc(numbers):
    """
    6 7 8 9 1 2 3 4 5 에서 최장 증가 부분 수열을 구한다고 하면
    중간 과정에서의 숫자 순서는 크게 중요하지 않다
    결국, 중간 과정에서 1 2 8 9 라고 나온다고 하더라도 숫자 순서가 맞지 않으니 틀렸다고 할 수 없다
    왜냐하면 저 순서로 최종 수열이 나오더라도 최장 증가 수열의 길이는 6 7 8 9 와 같은 4 이기 때문!
    """
    per = [0]  # 수열을 담을 리스트
    answer = 1  # 수열의 길이
    for num in numbers:

        if num >= per[-1]:  # 현재 번호가 수열의 최댓값 이상인 경우
            per.append(num)
            answer += 1
            continue

        # 최댓값 미만인 경우
        for i in range(1, answer + 1):  # 앞에서부터 현재 숫자 이상의 숫자가 나올 때까지 본다
            if num <= per[i]:
                per[i] = num  # 현재 숫자 이상의 숫자가 나온 위치를 현재 숫자로 바꾼다
                break

    return answer - 1


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    max_length = 0
    max_inc_per(0, numbers, 0, 0)
    print(f'#{test_case} {max_length}')
    print(f'#{test_case} {max_inc(numbers)}')

'''
9
6 7 8 9 1 2 3 4 5
9
6 7 20 21 8 9 10 11 12
'''