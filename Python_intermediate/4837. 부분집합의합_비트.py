import sys

sys.stdin = open("input.txt")

def sum_subset(ele_number, ele_sum):
    """
    :param ele_number: 포함해야 하는 원소의 개수가 주어진다.
    :param ele_sum: 원소들을 모두 더했을 때 나와야 하는 값이 주어진다.
    :return: 원소의 개수와 합이 모두 조건에 맞는 부분집합의 개수를 반환
    """
    # 1부터 12의 숫자를 원소로 가지는 집합을 하나 만들자
    original_set = [i for i in range(1, 13)]
    result = 0

    # 부분집합을 생성!
    for i in range(1 << 12):

        # 각 부분집합의 원소를 담을 빈 리스트와
        # 각 부분집합이 원소를 몇 개 가지고 있는지 판단할 수 있게 변수를 생성하자
        temp = []
        temp_ct = 0

        for j in range(12):
            if i & (1<<j):
                # print(original_set[j], end=" ")
                temp.append(original_set[j])
                temp_ct += 1

        # print(temp)
        # 이 방식으로 부분집합을 구하면
        # 원소들이 오름차순으로 정렬되고
        # 제일 큰 원소를 포함하는 부분집합이 만들어진다
        # 그래서 제일 큰 원소가 조건에서 주어진 합보다 커지먼
        # 그 이후는 진행하지 않는다
        if temp_ct >= 1 and temp[-1] > ele_sum:
            break

        # 만약 가지고 있는 원소의 개수가 조건과 같다면 합을 구하자
        if temp_ct == ele_number:
            temp_sum = 0

            for number in temp:
                temp_sum += number

            if temp_sum == ele_sum:
                result += 1

    return result


T = int(input())

for test_case in range(1, T + 1):
    ele_number, ele_sum = map(int, input().split())
    print("#{} {}".format(test_case, sum_subset(ele_number, ele_sum)))