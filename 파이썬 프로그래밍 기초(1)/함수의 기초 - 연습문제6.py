num_list = [2,4,6,8,10]

judge_list = [5, 10]

def judge_in_list(a):
    answer = []
    for i in range(len(a)):
        if a[i] in num_list :
            answer.append(str(a[i]) + ' => True')
        else :
            answer.append(str(a[i]) + ' => False')
    return answer
print(num_list)
print("{}\n{}".format(judge_in_list(judge_list)[0], judge_in_list(judge_list)[1]))

#다른 사람 풀이
def Check_for_existence(k, t):
    print("%d => " % t, end="")
    # t가 k안에 있다면
    if t in k:
        print(True)
    else:
        print(False)


k = [2, 4, 6, 8, 10]
print(k)
Check_for_existence(k, 5)
Check_for_existence(k, 10)