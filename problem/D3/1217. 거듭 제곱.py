def power(number, p_ct):
    if p_ct == 1:
        return number
    else:
        p_ct -= 1
        return number * power(number, p_ct)

for _ in range(10):
    test_case = int(input())
    number, p_ct = map(int, input().split())
    print("#{} {}".format(test_case, power(number, p_ct)))