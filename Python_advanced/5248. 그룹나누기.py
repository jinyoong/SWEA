import sys

sys.stdin = open('input.txt')


def solution(num, couple):

    people = {i for i in range(1, num+1)}
    group = []

    for ele in couple:  # ele: (a, b) 형태
        g1 = set()
        g2 = set()

        for i in range(len(group)):  # 그룹 중 a 를 포함하는 그룹이 있는지 확인
            if ele[0] in group[i]:  # a 를 포함하는 그룹이 있으면 g1 에 저장
                g1 = group.pop(i)
                break

        for i in range(len(group)):  # 남아있는 그룹 중 b 를 포함하는 그룹이 있는지 확인
            if ele[1] in group[i]:  # b 를 포함하는 그룹이 있으면 g2 에 저장
                g2 = group.pop(i)
                break
        
        if g1 and g2:  # a, b 를 포함하는 그룹이 각각 있고, (a, b) 연결에 의해 합쳐져야 하니까 합쳐서 저장
            group.append(g1.union(g2))

        elif g1:  # a 가 들어있는 그룹만 있는 경우 해당 그룹에 b 추가
            group.append(g1.union(ele))

        elif g2:  # b 가 들어있는 그룹만 있는 경우 해당 그룹에 a 추가
            group.append(g2.union(ele))

        else:  # 지금까지 a, b 를 포함한 그룹이 하나도 없는 경우 {a, b} 그룹을 새롭게 만들어서 추가
            group.append(set(ele))

        people -= set(ele)  # 한 번 나온 인원들은 볼 필요 없으니 제거

    return len(group) + len(people)


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    couple = [(lst[2*i], lst[2*i+1]) for i in range(M)]
    print('#{} {}'.format(test_case, solution(N, couple)))
