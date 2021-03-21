str_ex = 'abcdef'
num_list = [0, 1, 2, 3, 4, 5]
dict_list = dict(zip(str_ex, num_list))
# zip()함수를 사용하면 순서에 맞는 두 인자를 가지고 작업한다.
for k, v in dict_list.items():
    # 딕셔너리의 키와 값을 보고 싶으면 item()을 써야 한다.
    print("{}: {}".format(k, v))