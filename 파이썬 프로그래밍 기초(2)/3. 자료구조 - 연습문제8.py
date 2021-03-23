str_input = input()
upper_ct = 0
lower_ct = 0

for i in str_input:
    if i.isupper():
        upper_ct += 1
    elif i.islower():
        lower_ct += 1
print("UPPER CASE {}".format(upper_ct))
print("LOWER CASE {}".format(lower_ct))