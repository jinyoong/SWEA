str_input = input()
str_list = str_input.split(", ")
str_list.sort()
for i in str_list:
    if str_list.index(i) == len(str_list) - 1:
        print(i)
    else:
        print(i,end=", ")