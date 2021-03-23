str_input = input()
str_set = set(str_input)
#print(str_set)

for i in str_set:
    temp = 0
    for j in str_input:
        if i == j:
            temp += 1
    print('{},{}'.format(i,temp))