def more_big_multi(list1, list2, x, y):
    """
    두 개의 리스트가 들어오는데 작은 리스트를 움직인다
    작은 리스트의 길이가 x이고 긴 리스트의 길이가 y라고 하자
    이때, 작은 리스트의 0번째 인덱스가 이동할 수 있는 위치는
    긴 리스트의 0번째 인덱스부터, y-x번째 인덱스까지이다
    즉, 반복문을 통해 시작점을 바꾸면서 위치에 맞는 요소들끼리 곱한 뒤
    총합을 구해 리스트에 추가한 뒤 최댓값을 반환하면 된다
    """
    result = []
    for i in range(0, y-x+1):
        temp = 0
        for j in range(x):
            temp += list1[j] * list2[i+j]
        result.append(temp)
    return max(result)

T = int(input())
for test_case in range(1, T+1):
    x, y = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    if x > y:
        big = list1
        small = list2
        x, y = y, x
    else:
        big = list2
        small = list1
    print(f'#{test_case} {more_big_multi(small, big, x, y)}')