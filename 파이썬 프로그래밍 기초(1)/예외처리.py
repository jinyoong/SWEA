data_list = list(range(1, 11))

print("data_list: {}".format(data_list))

try:
    num = int(input("인덱스로 사용할 숫자를 입력하세요: "))
    print("[{}]: {}".format(num, data_list[num]))
# 입력한 숫자가 0 ~ 9 사이의 숫자가 아닐 경우 실행
except IndexError as exception:
    print(exception)
# 입력값이 숫자가 아닐 경우 실행
except ValueError as exception:
    print(exception)
# num 대신에 num1 등 위의 두 가지 경우가 아닌 예외 상황일 경우 실행
except Exception as exception:
    print(exception)


# 함수를 활용한 예외 처리

def input_index():
    # 함수 내에서 직접 에러를 처리하는 것이 아니라,
    # 예외가 발생한 곳으로 전달하는 방법의 함수
    num = 0
    try:
        num = int(input("인덱스로 사용할 숫자를 입력하세요: "))
    except ValueError as exception:
        raise exception
    else:
        return num


def print_in_bounds(list, index):
    # 함수 내에서 예외를 직접 처리하는 방식
    value = 0
    try:
        value = list[index]
    except IndexError as exception:
        print("{} {}".format(type(exception), exception))
        index = len(list) - 1
        print("인덱스는 0 ~ {}까지 사용할 수 있습니다.".format(index))
        value = list[index]
    finally:
        print("[{}]: {}".format(index, value))


data_list = list(range(1, 11))

try:
    num = input_index()
    print_in_bounds(data_list, num)
# 입력값이 숫자가 아닐 경우 실행
except ValueError as exception:
    print(exception)
# num 대신에 num1 등 위의 두 가지 경우가 아닌 예외 상황일 경우 실행
except Exception as exception:
    print(exception)