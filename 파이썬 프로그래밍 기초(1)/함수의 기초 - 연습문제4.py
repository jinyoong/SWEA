fibo_num = int(input())


def make_fibo(fibo_num):
    fibo_list = [1, 1]
    for i in range(2, fibo_num):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])


    return fibo_list


print(make_fibo(fibo_num))

