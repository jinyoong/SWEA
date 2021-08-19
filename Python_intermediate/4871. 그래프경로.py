import sys

sys.stdin = open("input.txt")


def graph_line(graph, s):
    """
    시작 노드에서 가장 먼저 나오는 번호로 가보자
    끝까지 간 지점이 도착 지점이 아니라면 바로 전으로 돌아가서 다음 번호 노드로 가는 과정을 반복해
    도착 지점에 도착하면 1 을 반환하고
    모든 지점을 갔는데도 도착 지점에 갈 수 없었다면 0 을 반환하자
    """
    global result

    # 출발 노드와 도착 노드가 같다 => 이미 도착한 상태!!
    if s == g:
        result = 1

    # 해당 노드로부터 갈 곳이 아무 곳도 없다! 돌아가자
    elif 1 not in graph[s]:
        pass

    # 현재 노드에서 출발할 곳이 존재한다
    else:
        for i in range(1, v + 1):
            # 가장 먼저 갈 수 있는 노드부터 접근해보자
            if graph[s][i] == 1:
                new_s = i
                graph_line(graph, new_s)
                # 만약 지금 도착하는 경로가 하나라도 나왔다면
                # 반복문을 종료
                if result == 1:
                    break

    return result


T = int(input())

for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[0] * (v + 1) for _ in range(v + 1)]
    for _ in range(e):
        n1, n2 = map(int, input().split())
        # 위로 돌아가는 경우가 없게 하기 위해서
        # 이미 경로가 표시된 경우에는 경로를 표시하지 않는다!
        if graph[n1][n2] != 1:
            graph[n1][n2] = 1
    s, g = map(int, input().split())
    result = 0
    print("#{} {}".format(test_case, graph_line(graph, s)))
