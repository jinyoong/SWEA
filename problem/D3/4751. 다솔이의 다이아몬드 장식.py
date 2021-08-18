def diamond(word):
    result = [[]] * 5
    for i in range(5):
        result[0] = ['..#.'] * len(word)
        result[1] = ['.#.#'] * len(word)
        for alpha in word:
            result[3] += ['#.{}.'.format(alpha)]
        result[3] = ['.#.#'] * len(word)
        result[4] = ['..#.'] * len(word)
    result[0] += ['.']
    result[1] += ['.']
    result[2] += ['#']
    result[3] += ['.']
    result[4] += ['.']
    return result

T = int(input())

for _ in range(T):
    word = input()
    for line in diamond(word):
        print(''.join(line))
