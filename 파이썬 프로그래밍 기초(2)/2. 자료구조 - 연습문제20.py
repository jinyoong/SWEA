num_input = input()

num_list = [int(i) for i in num_input.split(",") if int(i) % 2 == 1]
for k in num_list:
    if num_list.index(k) == len(num_list) - 1:
        print(k)
    else:
        print(k,end=", ")