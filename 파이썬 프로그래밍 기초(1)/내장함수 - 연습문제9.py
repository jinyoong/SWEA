int_list = range(1, 11)

filter_list = list(filter(lambda x: x % 2 == 0, int_list))

map_list = list(map(lambda x: x ** 2, filter_list))

print(map_list)

