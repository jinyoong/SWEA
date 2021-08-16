import sys

sys.stdin = open("input.txt", encoding='UTF-8')


def search_str(find, search):
    # 고지식한 패턴 검색 방법을 사용하기 위해
    # 원본 문자열의 몇 번째 인덱스까지 살펴볼지 정해야 한다

    result = 0
    end = len(search) - len(find)
    # 원본 문자열에서 find 를 찾아야 하므로 원본 문자열의 마지막 인덱스는
    # len(search) - len(find) 여야 한다

    for i in range(end + 1):
        # 원본 문자열의 시작인덱스를 1 씩 증가시켜가면서
        # 해당 인덱스부터 find 의 길이만큼 보았을 때
        # find 와 동일하다면 결과를 1 증가시켜 주자
        if search[i:i+len(find)] == find:
            result += 1
    return result


for _ in range(10):
    test_case = int(input())
    find = input()
    search = input()
    print("#{} {}".format(test_case, search_str(find, search)))
