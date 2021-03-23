str_input = input()
str_list = list(set(str_input.split(" ")))
str_list.sort(reverse=False)
print(",".join(str_list))

# 다른 풀이
t_str = input()
temp = t_str.split(' ')
temp = set(temp)
temp = sorted(temp)
print(",".join(temp))