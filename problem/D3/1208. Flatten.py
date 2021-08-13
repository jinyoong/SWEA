def dump(n, box_list):
    """
    :param n: 평탄화 작업을 할 수 있는 횟수
    :param box_list: 각 상자의 높이가 적혀져 있는 길이 100짜리 리스트
    :return: n 번의 평탄화 작업 이후 최고점과 최저점의 차이
    상자의 높이는 1 ~ 100 의 숫자들이므로 카운팅 정렬을 이용하여 먼저 정렬하자
    정렬한 이후 평탄화 작업을 진행하자
    """

    # 카운팅 정렬과정

    temp = [0] * 101
    # 1 ~ 100 의 숫자들이 총 몇 번 나오는지 개수를 저장하기 위한 리스트

    for num in box_list:
        temp[num] += 1
    # temp 리스트에서 상자의 높이에 해당하는 인덱스 위치에 1을 더해준다

    for i in range(1, 101):
        temp[i] = temp[i] + temp[i-1]
    # 카운팅 정렬을 위해 temp 리스트의 요소들을 누적합 형태로 바꾸어 준다

    result = [0] * 101
    for box in box_list[::-1]:
        result[temp[box]] = box
        temp[box] -= 1
    result = result[1:]
    # result 리스트에 카운팅 정렬 결과를 넣은 뒤
    # 0을 가지는 result 의 맨 앞 요소를 제외한 나머지 100개의 요소만 가진 result 리스트로 변환

    # 정렬된 리스트를 이용하여 평탄화 작업을 진행하자
    # 상자를 쌓을 때 제일 작은 숫자가 여러 개 있다면 리스트의 가장 오른쪽에 위치한 요소에 쌓고,
    # 제일 큰 숫자가 여러 개 있다면 리스트의 가장 왼쪽에 위치한 요소를 빼 줄 것이다.
    # [1, 1, 2, 3, 4, 5, 6, 6, 7] 의 경우 1번째 평탄화 작업을 통해
    # [1, 2, 2, 3, 4, 5, 6, 6, 6] 으로 변하고, 2번째 평탄화 작업을 진행하면
    # [2, 2, 2, 3, 4, 5, 5, 6, 6] 이 된다.
    # 이러한 방식을 통해 가장 왼쪽의 값이 항상 최솟값이 되고,
    # 가장 오른쪽의 값은 항상 최댓값을 유지하게 된다.
    for i in range(n):
        min_idx = 0
        max_idx = -1
        # 가장 작은 요소와 가장 큰 요소의 위치를 찾기 위해 위의 값으로 초기화 한다

        # 가장 작은 요소를 찾는 과정
        while True:
            # 먼저 앞에서부터 인접한 2개의 요소의 대소관계가 < 형태일 때까지 min_idx 를 1씩 증가시키자
            # < 형태가 된다면 앞의 요소가 해당 리스트에서 제일 작은 값을 가진 것이라 할 수 있으므로
            # 앞의 요소에 1을 더해준다
            if result[min_idx] < result[min_idx + 1]:
                result[min_idx] += 1
                break
            else:
                min_idx += 1

        # 가장 큰 요소를 찾는 과정
        while True:
            # 뒤에서부터 인접한 2개의 요소의 대소관계가 < 형태일 때까지 max_inx 를 1씩 감소시키자
            # < 형태가 된다면 뒤의 요소가 해당 리스트에서 제일 큰 값을 가진 것이라 할 수 있으므로
            # 뒤의 요소에 1을 빼준다.
            if result[max_idx - 1] < result[max_idx]:
                result[max_idx] -= 1
                break
            else:
                max_idx -= 1
    return result[-1] - result[0]



for test_case in range(1, 11):
    n = int(input())
    box_list = list(map(int, input().split()))
    print("#{} {}".format(test_case, dump(n, box_list)))