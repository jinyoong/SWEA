str_input = input()

str_list = str_input.split(" ")

answer = ""

for i in range(-1, -len(str_list)-1,-1):
    if i == -len(str_list):
        answer += str_list[i]
    else:
        answer += str_list[i] + ' '

print(answer)

# 더 좋은 풀이

t_str = input()
t_list = t_str.split(" ")
t_list.reverse()
# 해당 리스트를 반대로 뒤집는다.
print(" ".join(t_list))
# t_list의 항목들의 사이에 공백을 추가하여 연결한다.