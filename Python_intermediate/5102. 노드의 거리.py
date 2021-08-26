def adj_list(lst, node_ct):  # 인접리스트 만들기, 방향 관계 없이 연결점 모두 추가
    output_list = [[0] * (node_ct + 1) for _ in range(node_ct + 1)]
    for ele in lst:  # ele = [a, b] 면 a번 노드와 b번 노드가 연결
        output_list[ele[0]][ele[1]] = ele[1]  # a 번 노드가 갈 수 있는 노드로 b 노드 추가
        output_list[ele[1]][ele[0]] = ele[0]  # b 번 노드가 갈 수 있는 노드로 a 노드 추가
    return output_list


def pass_node(node_list, can_go, end):
    visited = [False] * (v + 1)  # 한 번 방문한 노드는 돌아가지 않게 하기 위해 visited 생성
    while can_go:  # 선택할 수 있는 출발 노드가 없어질 때까지 반복
        start_pt, distance = can_go.pop(0)  # 현재 노드와 현재 노드까지의 거리 저장
        visited[start_pt] = True

        if end in node_list[start_pt]:  # 현재 노드에서 갈 수 있는 노드들 중 도착 노드가 있다면
            return distance + 1  # 거리에 1을 더한 뒤 함수 종료

        if not node_list[start_pt]:  # 현재 노드에서 갈 수 있는 노드들이 한 곳도 없는 경우
            continue  # 다음 노드로 출발점을 옮기자

        for arrive in node_list[start_pt]:
            if arrive and not visited[arrive]:  # 갈 수 있는 노드가 이미 지나친 노드면 넘어간다
                can_go.append([arrive, distance+1])
    return 0


T = int(input())

for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    input_list = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())
    nodes = adj_list(input_list, v)
    print('#{} {}'.format(test_case, pass_node(nodes, [[s, 0]], g)))
