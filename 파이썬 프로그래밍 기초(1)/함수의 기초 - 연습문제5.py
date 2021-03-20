original_list = [1,2,3,4,3,2,1]


def ch_list(a):
    new_list = []
    new_list.append(a[0])
    for i in range(1,len(a)):
        if a[i] not in new_list :
            new_list.append(a[i])
    return new_list


print(original_list)
print(ch_list(original_list))