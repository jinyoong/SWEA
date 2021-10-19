def enq(n):  # 최대힙 삽입 연산
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p >= 1 and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2


def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]  # 맨 끝의 리프 노드 값을 루트 노드로
    last -= 1  # 해당 리프 노드를 없는 셈 치기
    p = 1  # 부모의 초기 값
    c1 = 2*p
    c2 = 2*p + 1

    # 자식이 있으면 비교해야 한다
    # 왼쪽 자식만 있는 경우 => 2*p == last 이게 된다
    while c1 <= last:  # 자식이 하나라도 있으면
        if c2 <= last:  # 자식이 둘이면

            if tree[c1] >= tree[c2] and tree[c1] > tree[p]:  # 왼쪽 자식이 더 큰 값을 가지는 경우
                tree[c1], tree[p] = tree[p], tree[c1]
                p = c1
            elif tree[c1] < tree[c2] and tree[c2] > tree[p]:  # 오른쪽 자식이 더 큰 값을 가지는 경우
                tree[c2], tree[p] = tree[p], tree[c2]
                p = c2
            c1 = p*2
            c2 = p*2+1
        else:  # 왼쪽자식만 존재하는 경우
            if tree[c1] > tree[p]:
                tree[c1], tree[p] = tree[p], tree[c1]
            break


tree = [0] * 101
last = 0
a = [7, 2, 3, 9, 5]
for x in a:
    enq(x)
