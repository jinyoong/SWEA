def palindrome(word):
    result = 1
    for i in range(len(word)):
        if word[i] != word[-i-1]:
            result = 0
            break
    return result

T = int(input())

for test_case in range(1, T+1):
    word = input()
    print(f'#{test_case} {palindrome(word)}')