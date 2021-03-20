num_list = list(map(int, input().split(",")))

def square_num(x):
    print('square({}) => {}'.format(x, x**2))

for i in num_list:
    square_num(i)