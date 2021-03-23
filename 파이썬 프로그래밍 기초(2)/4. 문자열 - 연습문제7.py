str_input = input()
str_list = [i for i in str_input if str_input.index(i) % 2 == 0]
print("".join(str_list))