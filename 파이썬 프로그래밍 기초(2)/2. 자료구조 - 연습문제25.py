num_list = [12, 24, 35, 70, 88, 120, 155]

answer = [i for i in num_list  if not (num_list.index(i) == 0 or num_list.index(i) == 4 or num_list.index(i) == 5)]
print(answer)