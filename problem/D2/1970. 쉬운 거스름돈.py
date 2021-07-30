def need_money(money):
    money_dict = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}
    for element in money_dict:
        if element > money:
            pass
        else:
            money_dict[element] += money // element
            money %= element
        if money == 0 or 1 <= money <= 9:
            return list(money_dict.values())

T = int(input())

for test_case in range(1, T+1):
    money = int(input())
    print(f'#{test_case}')
    print(*need_money(money))