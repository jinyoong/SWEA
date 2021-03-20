t = int(input())

def fac_num(n):
    answer = 1
    for i in range(1,n+1):
        answer *= i
    return answer

print(fac_num(t))