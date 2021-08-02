def water_price(p, q, r, s, w):
    # A사의 경우, 사용량 w에 p를 곱하여 해당 달의 수도 요금을 계산한다
    A_price = p * w

    # B사의 경우 먼저 기준 리터 r보다 사용량 w가 더 큰지, 작은지 판단해야 한다
    if r >= w:
        # 사용량이 기준 리터보다 작거나 같은 경우
        # 기준 요금인 q만 내면 된다.
        B_price = q
    else:
        # 사용량이 기준 리터보다 많은 경우
        B_price = q + (w - r) * s

    if A_price < B_price:
        return A_price
    else:
        return B_price


T = int(input())

for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    print(f'#{test_case} {water_price(p, q, r, s, w)}')