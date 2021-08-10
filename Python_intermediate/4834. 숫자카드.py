import sys

sys.stdin = open("input.txt")

def number_card(n, number):
    """
    :param n: 입력받는 숫자가 n의 자리 숫자임을 의미
    :param number: 카드로 이루어진 수가 문자열
    :return: number 문자열에서 가장 많이 나온 숫자와 그 개수
    먼저 0 ~ 9 까지의 숫자의 개수를 담을 수 있는 temp 리스트를 만들고
    반복문을 통해 number의 모든 숫자에 접근하면서 temp 리스트 요소에 맞는 자리에 1씩 증가시키자
    """
    temp = [0] * 10
    max_num = 0
    for i in range(n):
        card_num = int(number[i])
        temp[card_num] += 1
        # 각각의 숫자가 몇 번 나오는지와 지금까지 가장 많이 나온 개수가 얼마인지 저장한다.
        if max_num < temp[card_num]:
            max_num = temp[card_num]
    # temp 리스트에 숫자들의 개수까지 입력이 되어있다.
    # 우리는 가장 많이 나온 숫자를 출력해야 하고, 장수가 같을 때는 큰 수를 출력해야 한다.
    # 따라서 temp의 마지막 인덱스부터 보며 max_num과 값이 같은 숫자를 출력하자
    for i in range(-1, -11, -1):
        if temp[i] == max_num:
            return 10+i, max_num


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    number = input()
    print("#{} {} {}".format(test_case, number_card(n, number)[0], number_card(n, number)[1]))