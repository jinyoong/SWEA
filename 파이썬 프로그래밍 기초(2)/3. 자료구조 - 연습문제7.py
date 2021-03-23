str_input = input()
digit_ct = 0
letter_ct = 0

for i in str_input:
    if i.isdigit():
        digit_ct += 1
    elif i.isalpha():
        letter_ct += 1
print("LETTERS {}".format(letter_ct))
print("DIGITS {}".format(digit_ct))