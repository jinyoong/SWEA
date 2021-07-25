num = int(input())

result = []

for i in range(1, num):
    if num % i == 0:
        result.append(i)
result.append(num)

print(*result)