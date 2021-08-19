import sys

sys.stdin = open("input.txt")


def test(sentence):
    """
    문장을 구성하는 요소를 하나씩 보면서 괄호가 있는지 살펴보자
    여는 괄호와 닫는 괄호를 담은 딕셔너리를 만드는데, 쌍이 맞게끔 값도 맞춰주자
    여는 괄호가 나오면 test_list 에 그대로 추가하고, 닫는 괄호가 나오면 조건문을 실행해야 한다
    """
    test_list = []
    open_dict = {'(': 0, '{': 1}
    close_dict = {')': 0, '}': 1}
    for alpha in sentence:
        if alpha in open_dict.keys():
            test_list.append(alpha)

        # 닫는 괄호가 나오는 경우
        elif alpha in close_dict.keys():

            # 닫는 괄호가 나왔는데 test_list 에 아무 괄호가 없는 경우 => 짝이 안맞음
            if not test_list:
                return 0

            # 닫는 괄호가 나왔고, 여는 괄호가 test_list 에 존재하지만 짝이 안 맞는 경우
            # 역시 0 을 반환
            elif close_dict[alpha] != open_dict[test_list[-1]]:
                return 0

            # 닫는 괄호가 나왔는데 test_list 에 있는 여는 괄호와 짝이 맞는 경우
            # test_list 의 마지막 괄호가 사라진다
            else:
                test_list.pop()

    # 문장 끝까지 진행했는데 test_list 에 무언가 남아있다는 말은
    # 닫는 괄호가 부족했다는 의미이므로 0 을 반환
    if test_list:
        return 0
    else:
        return 1


T = int(input())

for test_case in range(1, T + 1):
    sentence = input()
    print("#{} {}".format(test_case, test(sentence)))