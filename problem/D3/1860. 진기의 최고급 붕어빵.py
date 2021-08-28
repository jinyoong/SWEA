def boong(m, k, people):
    boong_list = [0] * 11112
    people_list = [0] * 11112

    for p in people:
        people_list[p] += 1

    temp = 0
    for i in range(1, len(boong_list)):
        if i % m == 0:
            temp += k
        boong_list[i] = temp

        if people_list[i] == 1:
            if boong_list[i] >= 1:
                temp -= 1
                people_list[i] = 0
            else:
                return 'Impossble'

        if 1 not in people_list:
            return 'Possible'


T = int(input())

for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    people = list(map(int, input().split()))
    print('#{} {}'.format(test_case, boong(m, k, people)))
