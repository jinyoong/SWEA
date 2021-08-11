def validify(number):
    """
    이 경우에는 number의 앞 2개의 숫자와 뒤에서 2개의 숫자를 이용해야 한다.
    AABB 로 주어지는 상황이라고 생각해보자
    1. AA가 만약 1 이상 12 이하라면 무조건 MMYY로 표현할 수 있다.
    즉, 이 경우에는 BB가 1 이상 12 이하라면 AMBIGUOUS를, 0 혹은 13 이상이라면 MMYY가 되는 것이다.
    2. AA가 만약 13 이상이라면 가능성이 있는 것은 YYMM 이다.
    즉, 이 경우에는 BB가 1 이상 12 이하라면 YYMM을, 13 이상이라면 NA가 되는 것이다.
    """
    AA = number // 100
    BB = number % 100
    if 1 <= AA <= 12:
        if 1 <= BB <= 12:
            return 'AMIGUOUS'
        else:
            return 'MMYY'
    else:
        if 1 <= BB <= 12:
            return 'YYMM'
        else:
            return 'NA'


T = int(input())

for test_case in range(1, T + 1):
    number = int(input())
    print(f'#{test_case} {validify(number)}')