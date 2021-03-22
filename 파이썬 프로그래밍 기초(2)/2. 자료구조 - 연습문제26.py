list1 = [1,3,6,78,35,55]
list2 = [12,24,35,24,88,120,155]
answer = []
for i in list1:
    if i in list2:
        answer.append(i)
print(answer)

answer2 = [i for i in list1 if i in list2]
print(answer2)