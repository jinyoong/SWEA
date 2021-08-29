import sys

sys.stdin = open("input.txt")


def back_room(student_list):
    # 학생들의 방이 1 ~ 400 까지 있으므로 temp 리스트를 하나 생성하자
    # 중요한 것은 홀수 방과 짝수 방이 마주보고 있어서 한 줄에는 200개의 방이 있다는 것
    temp = [0] * 201

    # 학생들이 이동한 경로를 살펴보고, 겹치는 부분이 1개라도 존재하면 기다려야 한다
    # 홀수 방과 짝수 방이 마주보고 있으므로
    # 조심해야 하는데
    # 2 => 4 로 가는 학생과, 1 => 3 으로 이동하는 학생의 경로는 똑같다고 볼 수 있게 된다
    # 즉, 짝수인 경우 방 번호를 절반으로 나누고, 홀수인 경우는 방 번호 절반에 1을 더하는 식으로
    # 새롭게 번호를 지정해서 비교하면 편하다
    for student in student_list:
        move_room = [0, 0]

        # 방 번호를 홀수, 짝수에 관계 없이 동일한 라인에서 출발한다고 볼 수 있게
        # 연산을 통해 바꿔주자
        for i in range(2):
            if student[i] % 2:
                move_room[i] = student[i] // 2 + 1
            else:
                move_room[i] = student[i] // 2

        # 만약 거꾸로 가는 학생이 있다면, 이를 반영해 주어야 하므로
        # 대소 관계를 이용하여 위치를 바꿔주자
        if move_room[0] > move_room[1]:
            move_room = move_room[::-1]
        for i in range(move_room[0], move_room[1] + 1):
            temp[i] += 1
    time = 0

    for num in temp:
        if time < num:
            time = num

    return time

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    student_list = [list(map(int, input().split())) for _ in range(n)]
    print("#{} {}".format(test_case, back_room(student_list)))