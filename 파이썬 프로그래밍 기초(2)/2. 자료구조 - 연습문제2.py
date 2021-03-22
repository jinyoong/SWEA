moum = ['a', 'e', 'i', 'o', 'u']

alpha_str = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

str_list = [alpha for alpha in alpha_str if alpha.lower() not in moum]
print(str_list)

for i in alpha_str:
    if i not in moum:
        if i == len(alpha_str) - 1:
            print(i)
        print(i,end="")