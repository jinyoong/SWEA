'''
마지막 정점 번호, 간선 수
6 8
0 1 0 2 0 5 0 6 4 3 5 3 5 4 6 4
'''

V, E = map(int, input().split())
edge = list(map(int, input().split()))

# 인접행렬
adjM = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adjM[n1][n2] = 1  # 이거만 입력하면 방향 그래프의 경우
    adjM[n2][n1] = 1  # 무향 그래프인 경우

# 인접 리스트
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
