import sys

sys.stdin = open('input.txt')


def rps_game(player_list):
    card_dict = {0: 3, 1: 1, 2: 2, 3: 3, 4: 1}
    player1 = player_list[0]
    player2 = player_list[1]
    if card_dict[player1[1] - 1] == player2[1]:
        return player1
    elif card_dict[player1[1] + 1] == player2[1]:
        return player2
    else:
        if player1[0] < player2[0]:
            return player1
        else:
            return player2


def tournament(idx_card):
    if len(idx_card) == 2:
        return rps_game(idx_card)
    if len(idx_card) == 1:
        return idx_card[0]
    if len(idx_card) % 2:
        middle_idx = (len(idx_card) + 1) // 2
    else:
        middle_idx = len(idx_card)//2
    group1 = idx_card[:middle_idx]
    group2 = idx_card[middle_idx:]
    a = tournament(group1)
    b = tournament(group2)
    return tournament([a, b])


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    cards = list(map(int, input().split()))
    player_card = list(enumerate(cards, start=1))
    game_stack = []
    print("#{} {}".format(test_case, tournament(player_card)[0]))

