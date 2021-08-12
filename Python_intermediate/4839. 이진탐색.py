import sys

sys.stdin = open("input.txt")


def binary_search(end_page, number, start_page=1):
    start = start_page
    end = end_page
    choice = (start + end) // 2

    if choice == number:
        return 1

    if choice > number:
        # 찾아야 하는 페이지보다 현재 중간 페이지가 더 큰 경우 => down!!
        # end 를 중간 페이지로 바꾼 뒤 다시 중간페이지를 펼친다
        end = choice

        return 1 + binary_search(end, number, start)

    else:
        # 찾아야 하는 페이지보다 현재 중간 페이지가 더 작은 경우 => up!
        # start 를 중간 페이지로 바꾼 뒤 다시 중간페이지를 펼친다
        start = choice

        return 1 + binary_search(end, number, start)

T = int(input())

for test_case in range(1, T + 1):
    end, number_a, number_b = map(int, input().split())
    print("#{}".format(test_case), end=" ")
    a_ct = binary_search(end, number_a)
    b_ct = binary_search(end, number_b)
    if a_ct < b_ct:
        print("A")
    elif a_ct > b_ct:
        print("B")
    else:
        print(0)