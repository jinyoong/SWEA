def typing(A, B):
    # 보이어-무어 알고리즘을 사용해보자
    start_idx = 0
    end_idx = len(B) - 1
    word_ct = 0
    while True:
        if end_idx >= len(A):
            # 만약 살펴볼 끝 인덱스가 길이를 넘어가면
            # 반복문 종료
            break
        else:
            if B[-1] == A[end_idx]:
                # 만약 현재 시작 ~ 끝 인덱스까지가 주어진 단어와 똑같다면
                for i in range(len(B)):
                    if B[i] != A[start_idx+i]:
                        break
                else:
                    word_ct += 1
                    # 다음은 현재 끝 인덱스의 바로 다음부터 시작하고
                    # 또 주어진 단어의 길이만큼 봐야하기 때문에 아래처럼 한다
                    start_idx = end_idx + 1
                    end_idx += len(B)
                    continue
            # 만약 현재 범위가 주어진 단어랑 다르다면
            # 2가지로 나뉜다.
            if A[end_idx] in B:
                temp_idx = B[::-1].index(A[end_idx])
                skip_pt = temp_idx
                start_idx += skip_pt
                end_idx += skip_pt
            else:
                start_idx = end_idx + 1
                end_idx += len(B)
    return len(A) - (len(B) * word_ct) + word_ct


def typing2(A, B):
    start_idx = 0
    end_idx = len(B) - 1
    word_ct = 0
    skip_dict = {}
    for idx, element in enumerate(B):
        if element not in skip_dict:
            skip_dict[element] = len(B) - idx - 1
    while True:
        if end_idx > len(A):
            # 만약 살펴볼 끝 인덱스가 길이를 넘어가면
            # 반복문 종료
            break
        if B[-1] != A[end_idx]:
            if A[end_idx] not in skip_dict.keys():
                start_idx += len(B)
                end_idx += len(B)
            else:
                start_idx += skip_dict[A[end_idx]]
                end_idx += skip_dict[A[end_idx]]
        else:
            for i in range(0, -len(B), -1):
                if A[end_idx + i] != B[i - 1]:
                    break
            else:
                word_ct += 1
            start_idx += len(B)
            end_idx += len(B)

    return len(A) - (word_ct * len(B)) + word_ct


T = int(input())

for test_case in range(1, T + 1):
    A, B = input().split()
    print("#{} {}".format(test_case, typing2(A, B)))
