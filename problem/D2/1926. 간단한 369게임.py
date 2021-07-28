game_369 = ['3', '6', '9']

def game(number):
    result = [0] * number
    for i in range(1, number+1):
        game_ct = 0
        for num in str(i):
            if num in game_369:
                game_ct += 1
        if game_ct == 0:
            result[i - 1] = i
        else:
            result[i - 1] = '-' * game_ct
    return result

N = int(input())
print(*game(N))