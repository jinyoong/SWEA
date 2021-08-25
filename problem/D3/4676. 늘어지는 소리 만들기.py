def long_word(word, points):
    new_word = ["z"] + list(word)
    for point in points:
        new_word[point] += '-'
    answer = ''.join(new_word)
    return answer[1:]

T = int(input())

for test_case in range(1, T + 1):
    word = input()
    n = int(input())
    points = list(map(int, input().split()))
    print("#{} {}".format(test_case, long_word(word, points)))
