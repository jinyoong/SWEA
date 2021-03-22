list1 = [12,24,35,24,88,120,155,88,120,155]

def del_list(x):
    answer = []
    for i in x :
        if i not in answer:
            answer.append(i)
    return answer
print(del_list(list1))