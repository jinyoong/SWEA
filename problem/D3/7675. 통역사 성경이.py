def func(n, sentence):
    full_stop = [".", "!", "?"]
    result = [0] * n
    sentence_idx = 0
    name_ct = 0
    for word in sentence:
        stop = False
        if word[-1] in full_stop:
            word = word[:-1]
            stop = True
        if word[0].isupper():
            if not word[1:] or (word[1:].islower() and word[1:].isalpha()):
                name_ct += 1
        if stop:
            result[sentence_idx] = name_ct
            sentence_idx += 1
            name_ct = 0

    return result

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    sentence = input().split()
    print(f"#{test_case}", end=" ")
    print(*func(n, sentence))
