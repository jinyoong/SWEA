q_list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]

a_list = []

for num in q_list:
    if num % 2 == 0:
        a_list.append(num)

print(a_list)