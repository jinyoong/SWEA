def word_dict(alpha1, alpha2):
    """
    두 단어 중 alpha1이 먼저 오는 단어이므로
    단어의 길이는 alpha2가 더 길거나 같을 수밖에 없다
    만약 두 단어의 길이가 다른 경우와 같은 경우로 나누어 생각하자
    """
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_dict = {}
    for idx, a in enumerate(alpha, start=1):
        alpha_dict[a] = idx
    if len(alpha2) != len(alpha1):
        if alpha2[:len(alpha1)] == alpha1:
            # alpha1의 길이만큼만 잘라낸 문자열이 alpha1과 같다면
            # 그 다음 문자가 a만 아니면 사이에 존재할 수 있다
            if alpha2[len(alpha1)] == 'a':
                return 'N'
            else:
                return 'Y'
        else:
            # 만약 잘라낸 문자열이 alpha1과 다르다?
            # 그럼 무조건 존재
            return 'Y'
    else:
        if (alpha.index(alpha1[0]) + 2) % 26 <= alpha.index(alpha2[0]):
            return 'Y'
        else:
            temp = list(alpha1)
            idx = -1
            while True:
                if alpha1[idx] == 'z':
                    temp[idx] = 'a'
                    idx -= 1
                else:
                    temp[idx] = alpha[alpha_dict[alpha1[idx]]]
                    break

    result =  ''.join(temp)
    if result < alpha2:
        return 'Y'
    else:
        return 'N'

T = int(input())


for test_case in range(1, T+1):
    a1 = input()
    a2 = input()
    a1.replace(' ', '')
    a2.replace(' ', '')
    print(f'#{test_case} {word_dict(a1, a2)}')