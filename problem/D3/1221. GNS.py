import sys

sys.stdin = open("input.txt")


def string_sort(alien_num_list):

    # 다른 행성에서 사용하는 숫자체계를 저장하자
    alien_num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR',
                 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    # 각 숫자들이 각각 몇 번 나왔는지 확인하자
    # 숫자가 0 ~ 9 까지 있기 때문에 인덱스와 똑같은 위치에 넣어주면 된다
    temp = [0] * 10

    for str_num in alien_num_list:
        temp[alien_num.index(str_num)] += 1

    # temp 에는 순서대로 0 ~ 9 까지의 숫자가 담겨있다
    # 출력해야 하는 순서도 마찬가지 이므로
    # [숫자] * 숫자의 개수 를 한 뒤 결과 리스트에 저장하자
    result = []

    # 숫자는 alien_num 에 있고, 각 숫자의 개수는 temp 리스트에 있으므로
    # enumerate 함수를 사용하여 인덱스와 값을 가져오자
    for idx, element in enumerate(alien_num):
        result += [element] * temp[idx]

    return result


T = int(input())

for test_case in range(1, T + 1):
    tc, number_ct = input().split()
    str_num_list = list(input().split())
    answer = string_sort(str_num_list)
    print(tc)
    print(*answer)
