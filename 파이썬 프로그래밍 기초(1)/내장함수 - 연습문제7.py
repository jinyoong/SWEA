int_list = range(1, 11)

filter_list = list(filter(lambda x : x % 2 == 0, int_list))
print(filter_list)