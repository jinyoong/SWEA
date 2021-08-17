def check2(str1, str2):
    # 보이어-무어 알고리즘 연습
    end_idx = len(str1) - 1
    start_idx = 0
    while True:
        if end_idx >= len(str2):
            return 0

        if str2[end_idx] == str1[-1]:
            # print("끝이 같습니다")
            # print("str1: {}, str2: {}".format(str1, str2[start_idx:end_idx+1]))
            # 문자열의 끝이 똑같은 경우
            if str1 == str2[start_idx:end_idx+1]:
                return 1
        else:
            # 문자열의 끝이 다른 경우
            if str2[end_idx] in str1:
                alpha = str2[end_idx]
                for i in range(-1, -(len(str1)+1), -1):
                    if str1[i] == alpha:
                        skip_pt = -(i + 1)
                        break
                start_idx += skip_pt
                end_idx += skip_pt
                continue

        start_idx = end_idx + 1
        end_idx += len(str1)


T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    print("#{} {}".format(test_case, check2(str1, str2)))