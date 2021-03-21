alpha_str = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
score_dict = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
score_list = list(map(lambda x: score_dict[x], alpha_str))

answer = 0
for i in score_list:
    answer += i
print(answer)

# sum(score_list)로도 총 합을 구할 수 있다.
