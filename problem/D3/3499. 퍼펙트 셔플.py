def shuffle(n, cards):
    """
    카드가 6 장이라면 0 ~ 2 번 카드는 2배의 인덱스 위치로 이동하게 되고,
    3 ~ 5 번 카드는 각각 1, 3, 5 위치로 이동하게 된다.
    카드가 5 장이라면 0 ~ 2 번 카드는 2배의 인덱스 위치로 이동하게 되고,
    3 ~ 4 번 카드는 각각 1, 3 위치로 이동하게 된다.
    """
    result = [''] * n
    for i in range((n-1) // 2 + 1):
        result[2 * i] = cards[i]

    holsoo_idx = 1
    for i in range((n-1) // 2 + 1, n):
        result[holsoo_idx] = cards[i]
        holsoo_idx += 2
    return result

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    cards = list(input().split())
    print("#{}".format(test_case), *shuffle(n, cards))
