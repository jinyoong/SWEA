count = 0
while True:
    n = input()
    if n:
        print(">> {}".format(n.upper()))
        count += 1
    else:
        break
    if count == 3:
        break