def password(numbers):
    # 리스트 맨 끝의 숫자와 겹치면
    # 리스트 맨 끝의 숫자를 없애는 식으로 진행하자
    # 스택...? 인걸까
    result = []
    for number in numbers:
        if result:
            # 비어있지 않은 경우
            if result[-1] == number:
                result.pop()
                continue
        # 결과 리스트가 비어있거나, 리스트의 끝 숫자와 현재 숫자가 다른 경우
        # 리스트의 맨 끝에 현재 숫자를 추가하자
        result.append(number)
    return ''.join(result)


for test_case in range(1, 11):
    n, numbers = input().split()
    print("#{} {}".format(test_case, password(numbers)))
