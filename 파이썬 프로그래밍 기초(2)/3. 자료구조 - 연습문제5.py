fruit = ['   apple    ','banana','  melon']

#a = '     aple  '
#print(a.strip())
# strip()함수가 공백 제거 함수이다.

fruit_dict = {i.strip(): len(i.strip()) for i in fruit}
print(fruit_dict)