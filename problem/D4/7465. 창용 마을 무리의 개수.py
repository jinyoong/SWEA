def solution(town):
    result = []
    total = set(i for i in range(1, N+1))

    for link in town:
        left = set()
        right = set()

        for i in range(len(result)):  # 왼쪽 사람이 속한 무리가 있는지 확인
            if link[0] in result[i]:
                left = result.pop(i)
                break

        for i in range(len(result)):  # 오른쪽 사람이 속한 무리가 있는지 확인
            if link[1] in result[i]:
                right = result.pop(i)
                break

        if left and right:  # 왼쪽, 오른쪽 각각이 속한 무리가 모두 있으면
            result.append(left.union(right))  # 두 무리를 하나로 합쳐준다
            continue

        if left:  # 왼쪽 사람만 속한 무리가 있으면
            result.append(left.union(set(link)))  # 해당 무리에 2명을 추가

        elif right:  # 오른쪽 사람만 속한 무리가 있으면
            result.append(right.union(set(link)))  # 해당 무리에 2명을 추가

        else:  # 두 사람 모두 어떠한 무리에도 속해 있지 않으면
            result.append(set(link))  # 새로운 무리를 만든다
        total -= set(link)

    return len(result) + len(total)


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(M)]
    print(f'#{test_case} {solution(town)}')

"""
6
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
7 2
1 3
3 4
6 3
1 2
3 4
5 2
10 5
1 2
8 2
3 6
9 6
7 8
10 6
1 2
8 2
3 6
7 8
6 8
9 10

# 정답
#1 2
#2 1
#3 5
#4 3
#5 5
#6 4
"""

# 1 2 7 8 / 3 6 9 / 4 / 5 / 10
# 1 2 8 6 7 3 / 4 / 5 / 9 10