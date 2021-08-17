import sys

sys.stdin = open("input.txt")


def alpha_ct(str1, str2):
    checked_list = []
    max_ct = 0
    # 가장 많이 들어 있는 글자의 개수를 출력하는 것
    # 먼저 str1 의 각 글자들에 접근하자
    for alpha_in_str1 in str1:
        alpha_ct = 0

        # alpha_in_str1 을 checked_list 에 넣자
        # 한 번 진행한 글자를 또 할 필요가 없게 하려고 조건을 넣은 것
        if alpha_in_str1 not in checked_list:
            checked_list.append(alpha_in_str1)

            # str1 의 각 글자들과 같은 글자의 수를 세기 위해 alpha_ct 를 초기화 하자
            for alpha_in_str2 in str2:
                if alpha_in_str1 == alpha_in_str2:
                    alpha_ct += 1
                    if max_ct < alpha_ct:
                        max_ct = alpha_ct

    return max_ct


T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    print("#{} {}".format(test_case, alpha_ct(str1, str2)))