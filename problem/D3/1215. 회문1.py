def palindrome(n, alpha_list):
    """
    :param n: 8 x 8 크기의 2차원 배열 alpha_list 에서 찾아야 할 회문의 길이
    :param alpha_list: 회문을 찾을 2차원 배열
    :return: 길이가 n 인 회문의 개수를 반환
    """
    # 길이가 n 인 회문을 찾기 위해선 0번 인덱스부터 8 - n 인덱스까지 살펴야 한다.
    # 따라서 end_idx = 8 - n로 하자
    end_idx = 8 - n

    garo_ct = 0
    # 가로로 존재하는 회문의 개수를 파악
    for i in range(8):
        for j in range(end_idx + 1):
            if alpha_list[i][j:j + n] == alpha_list[i][j:j + n][::-1]:
                garo_ct += 1

    sero_ct = 0
    # 세로로 존재하는 회문의 개수를 파악
    for j in range(8):
        for i in range(end_idx + 1):
            temp = ""
            for k in range(n):
                temp += alpha_list[i+k][j]
            if temp == temp[::-1]:
                sero_ct += 1

    return garo_ct + sero_ct

for test_case in range(1, 11):
    n = int(input())
    alpha_list = []
    for _ in range(8):
        alpha = list(input())
        alpha_list.append(alpha)
    print("#{} {}".format(test_case, palindrome(n, alpha_list)))