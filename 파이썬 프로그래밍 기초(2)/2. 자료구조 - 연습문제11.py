def fibo(x):
    if x == 0 or x == 1:
        return 1
    return fibo(x-1) + fibo(x-2)

answer = [fibo(i) for i in range(10)]
print(answer)