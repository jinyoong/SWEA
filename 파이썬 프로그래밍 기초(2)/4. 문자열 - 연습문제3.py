str_input = input()
idx1 = str_input.find('://')
print("protocol: {}".format(str_input[:idx1]))
idx2 = str_input.rfind('/')
print("host: {}".format(str_input[idx1 + 3 : idx2]))
print("others: {}".format(str_input[idx2+1:]))