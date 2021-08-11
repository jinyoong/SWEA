import sys
# input을 파일로 받아오기

sys.stdin = open('input.txt')

def view(n, view_list):
    """
    view_list : 건물들의 세로 길이가 1차원 리스트로 주어진다
    return : 조망권이 확보된 세대들의 수를 반환한다.
    우선 max() 함수를 사용하지 않을 것이므로 모든 인덱스의 크기비교를 한다.
    max() 함수를 사용하면 max(view_list[i-2:i+3]) == view_list[i] 로 좀 더 짧게 할 수 있다.

    먼저 각 빌딩에 조망권이 확보된 세대가 존재하기 위해선 좌우 2개의 빌딩까지는 해당 빌딩보다 높이가 낮아야 한다.
    따라서 주어지는 view_list와 길이가 같으며 0으로 이루어진 temp 리스트를 만들자.
    반복문을 통해 모든 요소에 접근하는데
    i 번째 요소의 우측 2번째 요소(i+1, i+2) 모두 i 번째 요소보다 작은지 확인하자
    만약 두 요소 모두 작다면, 해당 temp 리스트의 해당 인덱스 값을 모두 -1로 바꾸자
    해당 위치의 건물들은 조망권 확보가 불가능하기 때문!
    """
    temp = [0] * n
    result = 0
    for idx in range(1, n-2):
        idx += 1
        if temp[idx] == 0:

            # 왼쪽 오른쪽 조망을 모두 확인
            if view_list[idx-2] < view_list[idx] and view_list[idx-1] < view_list[idx]:
                # 왼쪽 조망권 확보

                # 왼쪽 2개의 건물 중 가장 높은 건물의 높이를 구하자
                if view_list[idx-2] < view_list[idx-1]:
                    left_max = view_list[idx-1]
                else:
                    left_max = view_list[idx-2]

                if view_list[idx+1] < view_list[idx] and view_list[idx+2] < view_list[idx]:
                    # 오른쪽 조망권 확보

                    # 오른쪽 2개의 건물 중 가장 높은 건물의 높이를 구하자
                    if view_list[idx+1] < view_list[idx+2]:
                        right_max = view_list[idx+2]
                    else:
                        right_max = view_list[idx+1]

                    # 왼쪽 중 가장 큰 건물과 오른쪽 가장 큰 건물 중 더 큰 건물의 높이를 구하자
                    if left_max < right_max:
                        result += view_list[idx] - right_max
                    else:
                        result += view_list[idx] - left_max
                    temp[idx+1] = temp[idx+2] = -1
                else:
                    temp[idx] = -1
            else:
                temp[idx] = -1
            pass
        else :
            # temp[idx] = -1인 경우
            # 조망권 확보 불가
            continue
    return result


for test_case in range(1, 11):
    n = int(input())
    view_list = list(map(int, input().split()))

    print("#{} {}".format(test_case, view(n, view_list)))