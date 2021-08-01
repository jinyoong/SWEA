def zip_open(list_in):
    result = []
    temp = ''
    for element in list_in:
        while element[1] != 0:
            # print(f'{element[0]}가 아직 {element[1]}개 남아있습니다.')
            if len(temp) + element[1] > 10:
                temp += element[0]
                element[1] -= 1
            else:
                temp += element[0] * element[1]
                element[1] = 0
            if len(temp) == 10:
                result.append(temp)
                temp = ''
            if element == list_in[-1] and len(temp) + element[1] < 10:
                result.append(element[0] * element[1])
                break
    return result

T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    alpha_list = []
    for i in range(number):
        key, value = map(str, input().split())
        alpha_list.append([key, int(value)])
    print(f'#{test_case}')
    for p in zip_open(alpha_list):
        print(p)