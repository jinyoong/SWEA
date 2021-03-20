str1, str2 = input().split(", ")
def longer_str(x,y):
    if len(x) < len(y):
        return y
    else:
        return x


print(longer_str(str1, str2))