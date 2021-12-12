def need_paint(lst):  # 현재 줄을 하얀색, 파란색, 빨간색으로 칠하는데 필요한 칸의 개수를 반환
    need_w = need_b = need_r = 0
    for color in lst:
        if color != 'W':
            need_w += 1
        if color != 'B':
            need_b += 1
        if color != 'R':
            need_r += 1
    return [need_w, need_b, need_r]


def colors(flag, n):  # 1 ~ n-1 번째 줄을 모두 need_paint 함수를 적용한다
    color_list = [[] for _ in range(n)]
    for i in range(1, n-1):
        color_list[i] = need_paint(flag[i])
    return color_list  # W, B, R 로 칠하는데 필요한 칸의 개수들이 들어있는 2중 리스트


def russia_flag(flag, start_idx, idx, result):  # 러시아 국기처럼 칠하는 함수
    global min_num

    if min_num < result:  # 현재까지 칠한 결과가 최솟값보다 크면 가지치기
        return

    if idx == len(flag) - 1:  # 러시아 국기처럼 칠했으면
        min_num = result  # 최솟값 갱신
        return

    if idx == len(flag) - 2 and start_idx == 0:  # 현재까지 하얀색만 칠했으면 파란색 줄이 하나는 있어야 한다
        if min_num > result + flag[idx][1]:  # 파란색 줄로 만드는데 필요한 횟수를 더한 값이 최솟값보다 작으면
            min_num = result + flag[idx][1]  # 최솟값 갱신
        return min_num

    if start_idx == 2:  # 현재 줄을 빨간색으로 칠하면, 다음줄부터는 무조건 빨간색
        russia_flag(flag, start_idx, idx+1, result+flag[idx][start_idx])

    else:
        # 현재 줄이 빨간색이 아니면 다음 줄은 현재 줄의 색과 동일하거나 그 다음 색으로 칠할 수 있다.
        # 예를 들면 하얀색 => (하얀색 or 파란색), 파란색 => (파란색 or 빨간색)
        russia_flag(flag, start_idx, idx+1, result + flag[idx][start_idx])

        russia_flag(flag, start_idx+1, idx+1, result + flag[idx][start_idx+1])

    return min_num


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    input_list = [list(input()) for _ in range(n)]
    min_num = 5000  # 50 * 50 이니까 최솟값을 넉넉하게 초기화
    paint_list = colors(input_list, n)
    base_color_ct = 2 * m - input_list[0].count('W') - input_list[-1].count('R')  # 첫 줄과 마지막 줄은 고정!
    answer = russia_flag(paint_list, 0, 1, base_color_ct)
    print('#{} {}'.format(test_case, answer))
