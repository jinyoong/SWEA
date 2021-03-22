a, b = map(int, input().split(","))

answer = []
for i in range(a):
    temp = [i * j for j in range(b)]
    answer.append(temp)
print(answer)