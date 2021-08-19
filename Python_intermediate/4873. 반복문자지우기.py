import sys

sys.stdin = open("input.txt")


def clear_word(sentence):
    # 맨 처음에는 첫 문자를 넣어놓은 상태에서 시작하자
    # 그러니까 시작할 때 남아있는 문자는 1개 있는 상태!
    result = [sentence[0]]
    answer = 1

    # 1 번 인덱스의 문자부터 보기 시작한다
    for idx in range(1, len(sentence)):
        # 남아있는 문자가 있으면서 마지막 문자와 현재 문자가 같으면
        # 남아있는 문자의 맨 끝을 없애고, 남은 문자의 개수를 1 줄인다
        if result and sentence[idx] == result[-1]:
            answer -= 1
            result.pop()
        # 남아있는 문자가 없거나 같지도 않다면
        # 추가하고 1을 추가한다.
        else:
            answer += 1
            result.append(sentence[idx])

    return answer


T = int(input())

for test_case in range(1, T + 1):
    sentence = input()
    print("#{} {}".format(test_case, clear_word(sentence)))