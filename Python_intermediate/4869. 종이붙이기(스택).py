import sys

sys.stdin = open("input.txt")


def square(number):
    global two_ct
    global answer

    # 만약 남아있는 면적이 0 이면 멈추자!
    # 지금까지 나와 있는 2 의 개수만큼 2 에 거듭제곱을 해 준 값이
    # 해당 면적을 채우는 데 필요한 경우의 수라고 볼 수 있다
    if number == 0:
        answer += 2 ** two_ct
        return

    # 만약 남아있는 면적의 가로가 20보다 크면 20 x 20 부터 넣어보자
    if number >= 20:
        number -= 20
        two_ct += 1
        square(number)
        # 20 x 20 을 넣은 결과가 끝이 나면 이제 여기에 10 x 20 을 넣어줘야 하므로
        # 다시 원래대로 돌려놓자
        number += 20
        two_ct -= 1

    # 20을 먼저 넣고 돌아왔거나, 애초에 남은 공간이 10 이면 10 을 넣어준다
    if number >= 10:
        number -= 10
        square(number)
        number += 10
    return answer


result = [0] * 31
for i in range(10, 301, 10):
    answer = 0
    two_ct = 0
    result[i // 10] = square(i)

T = int(input())

for test_case in range(1, T + 1):
    number = int(input())
    print("#{} {}".format(test_case, result[number // 10]))