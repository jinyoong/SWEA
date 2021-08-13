import sys

sys.stdin = open("input.txt")

def box_num_change(N, Q, change_list):
    """
    :param N: 0 번호가 적힌 1 부터 N 까지의 상자
    :param Q: 현주의 규칙으로 숫자를 바꿀 작업 횟수
    :param change_list: 현주의 규칙이 적혀있는 2차원 리스트, 각 요소는 [L, R] 순서로 들어와 있다.
    :return: 규칙에 의해 바뀐 상자들의 번호
    박스의 번호는 모두 0 번에서 시작하게 되는데
    현주의 규칙에 의해 입력된 i번째(1 ~ Q) 작업에 의해 [L ~ R] 상자의 번호가 i 로 바뀐다
    주의해야 할 점은 상자와 작업의 순서는 모두 1부터 시작한다는 점!
    따라서 result = [0] * (N + 1) 로 만들자
    """
    result = [0] * (N+1)

    for i in range(1, Q + 1):
        # 1 부터 Q 까지의 번호를 상자에 붙인다.
        # i 번째 작업을 적용하는 박스에는 i 번호를 붙인다
        # 현주가 i 번째 번호를 붙일 상자는 change_list 의 (i - 1) 인덱스 규칙에 따르게 된다.
        # chagne_list 의 (i - 1) 인덱스에는 i 번이라고 숫자를 붙일 상자들의 시작 번호와 끝 번호가 적혀있다.
        start_num = change_list[i - 1][0]
        finish_num = change_list[i - 1][1]

        # 위의 시작 번호부터 끝 번호까지의 박스들에의 번호를 i 번으로 덮어 씌운다
        for box_num in range(start_num, finish_num + 1):
            result[box_num] = i

    return result[1:]

T = int(input())

for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    change_list = []
    for _ in range(Q):
        temp = list(map(int, input().split()))
        change_list.append(temp)
    print("#{}".format(test_case), end=" ")
    print(*box_num_change(N, Q, change_list))

# 2차원 리스트 사용하지 않는 경우

# T = int(input())
#
# for test_case in range(1, T + 1):
#     # 주어진 테스트 케이스만큼 반복
#
#     N, Q = map(int, input().split())
#     # N : 현주가 가진 1 ~ N 번까지의 N개의 상자
#     # Q : 일정 범위의 연속한 상자를 동일 숫자로 변경할 횟수
#
#     result = [0] * (N + 1)
#     # i 번째 박스에 접근하기 위해 (N + 1) 의 길이를 가진 리스트를 만든다
#
#     for rule_ct in range(1, Q+1):
#         # 현주가 적용하는 규칙이 횟수로 rule_ct 번째이면 해당 규칙의 박스들에게는 rule_ct 번호가 배정된다
#         # 현주가 적용할 규칙은 아래에서 주어진다
#
#         L, R = map(int, input().split())
#         # L : rule_ct 번이라고 번호를 붙일 박스의 시작 번호
#         # R : rule_ct 번이라고 번호를 붙일 박스의 끝 번호
#
#         result[L:(R + 1)] = [rule_ct] * (R - L + 1)
#         # L ~ R 번 박스에 rule_ct 번호를 붙여야 하므로 슬라이싱을 이용하고
#         # rule_ct 번호는 L ~ R 까지의 박스에 붙으므로 해당 숫자 리스트를 만들어준다
#
#     print("#{}".format(test_case), end = " ")
#     print(*result[1:])
