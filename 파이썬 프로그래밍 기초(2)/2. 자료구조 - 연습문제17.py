n = input()

num_list = list(map(int, n.split(",")))

def circle_len(x):
    return x * 2 * 3.141592

for num in num_list:
    if num_list.index(num) == len(num_list) - 1:
        print('%.2f' % circle_len(num))
    else:
        print('%.2f' % circle_len(num),end=", ")