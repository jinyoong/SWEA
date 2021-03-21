data_list = list(range(1, 21))

print("data_list : {0}".format(data_list))

map_list = list(map(lambda x: x + 5, data_list))

print("map_list : {0}".format(map_list))

# 아래의 코드는 유용하게 사용 가능하므로 잘 기억해두자
filter_list = list(filter(lambda x: x % 3 == 0, map_list))
# filter()함수는 인자 값을 조건과 비교하여 True, False 값을 반환하게 된다.
print("filter_list : {0}".format(filter_list))

map_str = input("항목 x에 대해 적용할 표현식을 입력하세요: ")
filter_str = input("항목 x에 대해 필터링할 조건의 표현식을 입력하세요: ")

map_list2 = list(map(lambda x: eval(map_str), data_list))
# data_list 의 각 항목에 대해 eval(map_str)함수의 반환값을 적용하여 리스트로 만든다.
# 예를 들어 x + 5 를 입력하면 각 항목에 5를 더한 값을 반환한다.
print("map_list2 : {}".format(map_list2))
filter_list2 = list(filter(lambda x: eval(filter_str), data_list))
# data_list 의 각 항목에 대해 eval(filter_str)함수의 반환값을 적용하여 리스트로 만든다.
# 예를 들어 x % 5 == 0 을 입력하면 해당 문자열에서 실행 가능한 표현식에 맞는 연산을 한다.
print('filter_list2 : {}'.format(filter_list2))
