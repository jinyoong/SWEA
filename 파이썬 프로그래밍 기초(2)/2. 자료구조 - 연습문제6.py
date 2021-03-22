num_input = int(input())

yaksu_list = []
for i in range(1, num_input + 1):
    if num_input % i == 0:
        yaksu_list.append(i)

print(yaksu_list)