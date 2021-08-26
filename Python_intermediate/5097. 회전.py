def revolve(numbers, length, cycle):
    front = 0
    rear = length
    for _ in range(cycle):  # 주어진 횟수만큼만 반복하자
        numbers[rear] = numbers[front]  # 맨 마지막 자리를 현재 맨 앞의 원소로 바꿔주자
        numbers[front] = 0  # 맨 끝으로 옮겼으니까 0으로!
        rear = (rear + 1) % (length + 1)  # 맨 마지막 자리 인덱스 변경
        front = (front + 1) % (length + 1)  # 맨 앞 자리 인덱스 변경
    return numbers[front]


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    input_list = list(map(int, input().split())) + [0]
    print('#{} {}'.format(test_case, revolve(input_list, n, m)))
