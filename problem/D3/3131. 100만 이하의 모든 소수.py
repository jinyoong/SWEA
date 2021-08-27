def prime():
    numbers = [True] * 1000001
    for num in range(2, 1000001):
        if numbers[num]:
            for j in range(num * 2, 1000001, num):
                numbers[j] = False
    return numbers


prime_number = prime()


for i in range(2, 1000001):
    if prime_number[i]:
        print(i, end=" ")
