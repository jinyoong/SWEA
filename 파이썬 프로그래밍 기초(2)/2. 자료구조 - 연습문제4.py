num_list = [int(input()) for i in range(5)]

total = 0
for num in num_list:
    total += num

print("입력된 값 {}의 평균은 {:.1f}입니다.".format(num_list,total / 5))