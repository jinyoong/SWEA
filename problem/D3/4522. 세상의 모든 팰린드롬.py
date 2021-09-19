def is_have_palindrome(word):
    length = len(word) // 2
    for i in range(length):
        if word[i] == word[-i-1]:
            continue
        if word[i] == '?' or word[-i-1] == '?':
            continue
        return "Not exist"
    return "Exist"


T = int(input())

for test_case in range(1, T+1):
    word = input()
    print(f'#{test_case} {is_have_palindrome(word)}')
