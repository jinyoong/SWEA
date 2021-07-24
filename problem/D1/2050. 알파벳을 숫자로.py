alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_num_dict = {}

i = 1
for alpha in alphas:
    alpha_num_dict[alpha] = i
    i += 1

alpha_input = input()

answer = [0] * len(alpha_input)

for i in range(len(alpha_input)):
    answer[i] = alpha_num_dict[alpha_input[i]]

print(*answer)