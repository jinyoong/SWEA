news = input()
small_alpha = 'abcdefghijklmnopqrstuvwxyz'
big_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alpha_change = {}

for i in range(26):
    alpha_change[small_alpha[i]] = big_alpha[i]

answer = ''

for alpha in news:
    if alpha in small_alpha:
        alpha = alpha_change[alpha]
    answer += alpha

print(answer)