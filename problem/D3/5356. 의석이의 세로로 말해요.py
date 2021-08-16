import sys

sys.stdin = open("input.txt")


def sero(input_str):
    # 입력받는 문자열은 5줄이 입력되지만
    # 각 줄의 문자열의 길이는 전부 다를 수 있다
    # 따라서 try ~ except 문을 사용하여 해당 인덱스로 문자열에 접근할 수 있을 때만
    # 결과 문자열에 저장하는 방법을 사용하자

    # 탐색을 시작할 열과, 최종 문자열을 담을 빈 문자열을 초기화하자
    start_idx = 0
    result = ''

    while True:
        # 각 열의 문자들을 모두 더할 임시 문자열
        # temp 를 빈 문자열로 초기화하자
        temp = ''

        # 문자열은 무조건 5 줄이 들어오므로 5번 반복한다
        for i in range(5):
            try:
                # 만약 i 행의 start_idx 열의 값을 alpha 에 저장한다고 해보자
                alpha = input_str[i][start_idx]
            except:
                # 위의 과정에서 오류(index out of range) 가 발생한다면
                # 그냥 넘어가고
                pass
            else:
                # 오류가 발생하지 않으면 temp 문자열에 추가한다
                temp += alpha

        # start_idx 열의 모든 문자를 나열했다면
        # 다음 열을 봐야 하므로 1을 더해주자
        start_idx += 1

        # 만약 start_idx 열의 5개 행을 전부 살펴봤는데
        # 전부 오류가 발생한다면 빈 문자열이 나올테니까
        # 이 경우에 while 문을 빠져나가자
        if temp:
            result += temp
        else:
            break

    return result


T = int(input())

for test_case in range(1, T + 1):
    input_str = [list(input()) for _ in range(5)]
    print("#{} {}".format(test_case, sero(input_str)))