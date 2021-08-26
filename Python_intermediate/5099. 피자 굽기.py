def bake_pizza(pizza, n, m):
    bake = [[]] * n
    front = 0
    pizza_number = [[i+1, pizza[i]] for i in range(m)]
    p_idx = 0
    p_ct = 0
    while True:
        if p_ct == 1 and p_idx == m:  # 넣을 수 있는 피자가 없고, 화덕 내에 남아있는 피자가 1개면 종료!
            for result in bake:  # 화덕에 마지막으로 남은 피자를 찾아서
                if result:
                    return result[0]  # 피자 번호를 반환

        if not bake[front] and p_idx < m:  # 화덕의 현재 위치에 피자를 넣을 수 있는 경우
            bake[front] = pizza_number[p_idx]  # 현재 위치에 피자를 넣자
            p_idx += 1  # 다음 피자 번호로 옮기고
            front = (front + 1) % n  # 피자를 넣을 위치를 다음으로 넘기자
            p_ct += 1  # 화덕에 들어있는 피자의 개수를 1 증가
            continue

        if len(bake[front]) != 0:  # 현재 위치에 피자가 있는 경우
            bake[front][1] //= 2  # 치즈를 반으로 줄이자
            if bake[front][1] == 0:  # 반으로 줄였더니 0 이라면
                bake[front] = []  # 현재 위치의 피자를 빼버리자
                p_ct -= 1  # 화덕 내의 피자 개수도 1 감소
                continue

        front = (front + 1) % n


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    print('#{} {}'.format(test_case, bake_pizza(input_list, n, m)))
