def multiplication(*params):
    # 가변형 인자를 전달받기 위해 *로 하였다. 즉, 몇 개를 입력할지 정해지지 않았을
    # 경우에 사용하는 것 같다.
    result = 1
    for i in params:
        if type(i) != int:
            return '에러발생'
            break
        result *= i
    return result


print(multiplication(1, 2, 3, "4", 5))
# *params 로 했기 때문에 함수 안에 몇 개의 인자가 들어가더라도 오류 없이 진행한다.
