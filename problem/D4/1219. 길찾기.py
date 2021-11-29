import sys

sys.stdin = open("input.txt")


def node_line(case_list, n):
    """
    한 줄로 입력되는 시작 노드와 연결 노드를 분리하자
    0번 인덱스의 자리에는 0번 노드에서 갈 수 있는 노드들을 담은 리스트가 들어간다
    즉, i 인덱스의 요소가 의미하는 것은
    i 번째 노드에서 출발해서 도착하는 노드들의 정보가 된다
    """
    # line_list : 도착 노드들을 담을 리스트
    # node_list : 일렬로 나열된 기본 리스트에서 2 개씩 쪼개서 담기 위한 리스트
    line_list = [[] for _ in range(100)]
    node_list = []

    # 원래 리스트는 출발 노드, 도착 노드 식으로 일렬로 나열되어 있기 때문에
    # [출발 노드, 도착 노드] 로 분리해서 node_list 에 담자
    for i in range(0, 2 * n, 2):
        node_list.append([case_list[i], case_list[i+1]])

    # 2 * ? 방법
    # for i in range(n):
    #     st = case_list[2 * i]
    #     ed = case_list[2 * i + 1]
    #     node_list.append([st, ed])

    # [출발 노드, 도착 노드] 를 담은 리스트를 완성했으면
    # 이제 line_list 에 값을 넣어줘야 한다
    for node in node_list:
        n1, n2 = node[0], node[1]
        line_list[n1].append(n2)

    return line_list


def road(line_list, s):
    global result
    # 출발 노드가 99번 노드가 되면 도착!
    if s == 99:
        result = 1

    # 만약 출발 노드에 연결된 노드들이 없으면
    # 돌아간다
    if not line_list[s]:
        pass

    else:
        # 0 -> 1 -> 2 -> 0 의 경우에는 계속 돌기만 할 수 있을 것 같다
        # 지나간 경로를 저장하는 리스트를 만들어야 하나....
        # 현재 노드에서 갈 수 있는 노드들에 순차적으로 접근한다
        for next_node in line_list[s]:
            # 도착 노드들로 넘어가야 하니까
            # 출발 노드를 해당 값으로 바꿔준다
            new_s = next_node
            road(line_list, new_s)
            if result == 1:
                break
    return result


for _ in range(10):
    test_case, n = map(int, input().split())
    case_list = list(map(int, input().split()))
    result = 0
    line_list = node_line(case_list, n)
    print("#{} {}".format(test_case, road(line_list, 0)))
