word = input()
def reverse_word(word):
    if word[::-1] == word :
        return "입력하신 단어는 회문(Palindrome)입니다."
    else:
        return '입력하신 단어는 회문(Palindrome)이 아닙니다.'

print(reverse_word(word))