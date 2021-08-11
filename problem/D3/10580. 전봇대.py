def power_pole(line_ct, list_in):
    """
    리스트는 2차원 리스트이며, 각 요소는 A, B, 기울기(전봇대 사이를 1로 봤을 경우)를 요소로 가진다.
    Ai 와 Bi의 끝점을 가지면서 연결된 직선들이므로
    교차점이 생기기 위해선 기울기가 다르면서 동시에 끝점이 서로 달라야 한다.
    예를 들면 1의 기울기가 2의 기울기보다 큰 경우,
    A1 < A2 이면서 B1 > B2 또는 A1 > A2 이면서 B1 < B2 여야 한다.
    따라서 먼저 Bi 크기를 기준으로 내림차순으로 리스트를 나열한 뒤
    기울기가 다른 직선 중 Ai가 더 큰 경우 결과에 1을 추가하는 식으로 진행하자
    """
    result = 0
    for i in range(line_ct - 1):
        for j in range(i+1, line_ct):
            if list_in[i][0] < list_in[j][0] and list_in[i][2] != list_in[j][2]:
                result += 1

    return result

T = int(input())

for test_case in range(1, T+1):
    line_list = []
    line_ct = int(input())
    for _ in range(line_ct):
        A, B = map(int, input().split())
        inc = B-A
        line_list.append([A, B, inc])
    line_list = sorted(line_list, key=lambda x: x[1], reverse=True)
    print(f'#{test_case} {power_pole(line_ct, line_list)}')