def below_average(list_ct, income_list):
    """
    평균을 먼저 구한 뒤 반복문을 통해 평균보다 작거나 같은 사람의 수를 세보자
    """
    result = 0
    mean_value = sum(income_list) / list_ct
    for income in income_list:
        if income <= mean_value:
            result += 1

    return result

T = int(input())

for test_case in range(1, T+1):
    list_ct = int(input())
    income_list = list(map(int, input().split()))
    print(f'#{test_case} {below_average(list_ct, income_list)}')