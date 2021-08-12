import sys

sys.stdin = open("input.txt")

def coloring_purple(numbers):
    """
    :param numbers: 2차원 배열의 형태로 색칠할 정보가 입력된다
    :return: 보라색으로 색칠된 영역의 개수 반환
    같은 색이 여러 번 칠해질 수 있으므로 조심하자
    """
    # 색칠을 시작할 하얀 도화지!
    original_list = [[0] * 10 for _ in range(10)]

    # 2차원 배열의 요소 리스트를 하나씩 뜯어본다
    for number in numbers:
        # 먼저 각 리스트의 순서가 시작 행, 시작 열, 끝 행, 끝 열, 칠할 색 으로 주어지므로
        # 이를 각각의 변수로 저장해 놓자
        start_low = number[0]
        end_low = number[2]
        start_col = number[1]
        end_col = number[3]
        color = number[4]

        # 도화지에서 주어진 영역에 색을 칠하기 시작
        # 같은 영역에 똑같은 색이 칠해지는 경우에는 변화가 있으면 안되니까
        # 같은 색만 칠해진 경우가 아니면 칠하자!
        for low in range(start_low, end_low + 1):
            for col in range(start_col, end_col + 1):
                if original_list[low][col] != color:
                    original_list[low][col] += color

    # 위와 같은 방법을 하게 되면
    # 파란색과 빨간색이 각각 1번 이상 칠해진 곳은 3 이상으로 표시가 되어 있게 된다
    # 따라서 3 이상인 부분의 수를 세어 주면 결과가 된다.
    result = 0
    for ori_low in range(10):
        for ori_col in range(10):
            if original_list[ori_low][ori_col] >= 3:
                result += 1

    return result

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    numbers = []
    for _ in range(n):
        number = list(map(int, input().split()))
        numbers.append(number)
    print("#{} {}".format(test_case, coloring_purple(numbers)))
