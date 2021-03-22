num_str = input()
answer = 0
for i in num_str:
    answer += int(i)

print(answer)

answer2 = [int(k) for k in num_str]
print(sum(answer2))