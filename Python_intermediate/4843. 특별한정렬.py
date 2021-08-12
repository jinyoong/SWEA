import sys

sys.stdin = open("input.txt")

def special_sort(idx, n, numbers):
    idx += 1
    if idx == n:
        return []

    if idx % 2:
        # 정렬하려는 인덱스가 홀수이면
        # 해당 인덱스 자리에는 idx 번째로 작은 수가 와야 한다.
        # 따라서 정렬된 리스트에서 idx 이후의 숫자들 중 가장 작은 값이 idx 위치에 있어야 한다

        # 선택 정렬 사용
        # idx 위치의 숫자를 가장 작은 값으로 보고 min_idx 와 min_value 를 초기화 하자
        min_idx = idx
        min_value = numbers[idx]

        # idx 뒤의 요소들 중에서 가장 작은 값을 찾기 위해
        # 만약 해당 값이 min_value 보다 작으면 최솟값을 바꿔주고
        # 해당 숫자의 위치를 min_idx 에 새롭게 저장한다
        for i in range(idx+1, n):
            if numbers[i] < min_value:
                min_value = numbers[i]
                min_idx = i

        # 최종적으로 나온 min_idx 가 idx 이후의 요소들 중 가장 작은 값이므로
        # 이 값과 idx 값을 서로 바꿔준다.
        numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]
        result = [numbers[idx]] + special_sort(idx, n, numbers)

    else:
        # 정렬하려는 인덱스가 짝수이면
        # 해당 인덱스 자리에는 idx + 1 번째로 큰 수가 와야 한다.
        # 마찬가지로 가장 큰 수를 고르는 방식은 선택 정렬을 이용

        max_idx = idx
        max_value = numbers[idx]

        for i in range(idx + 1, n):
            if numbers[i] > max_value:
                max_value = numbers[i]
                max_idx = i
        numbers[idx], numbers[max_idx] = numbers[max_idx], numbers[idx]
        result = [numbers[idx]] + special_sort(idx, n, numbers)

    return result[:10]

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    print("#{}".format(test_case), end=" ")
    print(*special_sort(-1, n, numbers))