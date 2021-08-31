def need_cards(cards):
    card_ct = len(cards) // 3
    have_card = [''] * card_ct
    for i in range(card_ct):
        have_card[i] = cards[3*i:3*i+3]

    card_list = []
    need_card = {'S': 13, 'D': 13, 'H': 13, 'C': 13}

    for card in have_card:
        temp = [card[0], int(card[1:])]
        if temp in card_list:
            return 'ERROR'
        card_list.append(temp)
        need_card[card[0]] -= 1

    result = []
    for alpha in 'SDHC':
        result.append(need_card[alpha])

    return result


T = int(input())

for test_case in range(1, T + 1):
    card_info = input()
    answer = need_cards(card_info)
    if type(answer) == str:
        print('#{} {}'.format(test_case, answer))
    else:
        print('#{}'.format(test_case), *answer)
