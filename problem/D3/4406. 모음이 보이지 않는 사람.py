def not_moum(sentence):
    moum = ['a', 'e', 'i', 'o', 'u']
    result = ""
    for alpha in sentence:
        if alpha not in moum:
            result += alpha
    return result

T = int(input())

for test_case in range(1, T + 1):
    sentence = input()
    print("#{} {}".format(test_case, not_moum(sentence)))