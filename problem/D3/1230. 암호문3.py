def secret_message(ori_cryp, commends):
    """
    :param ori_cryp: 원본 암호문
    :param commends: 명령어들이 담긴 2차원 리스트
    :return: 암호문을 명령어로 변경시킨 뒤 앞에서부터 10개의 암호문을 반환
    각각의 명령어에 접근해서 해당 명령어의 종류가 무엇인지 먼저 파악하자
    """
    for commend in commends:
        if commend[0] == 'I':
            # I 인 경우에는 [I, x, y, z] 식으로 입력이 된다
            # 원본 암호문의 x 인덱스에 y번 z 숫자들을 추가하므로
            # insert 를 이용하여 추가하자
            # 단, z 숫자들을 거꾸로 추가하자
            for number in commend[3:][::-1]:
                ori_cryp.insert(int(commend[1]), number)
        elif commend[0] == 'D':
            # D 인 경우에는 [D, x, y] 식으로 입력이 된다
            # 원본 암호문의 x 인덱스 자리를 y 번 삭제한다
            # pop 을 이용하여 삭제하자
            for i in range(int(commend[2])):
                ori_cryp.pop(int(commend[1]))
        else:
            # A 인 경우에는 [A, x, y] 식으로 입력이 된다.
            # 원본 암호문의 맨 끝에 x 번 y 숫자들을 추가한다.
            for number in commend[2:][::-1]:
                ori_cryp.append(number)
    return ori_cryp[:10]


for test_case in range(1, 11):
    # 처음부터 차례대로 원본 암호문의 길이, 원본 암호문, 명령어의 개수가 입력된다.
    ori_len = int(input())
    ori_se = list(map(int, input().split()))
    com_ct = int(input())

    # 명령어의 입력은 알파벳과 숫자가 합쳐져 들어오는데 이를 명령어 별로 나눠서 분리하자
    # 명령어 전체를 담을 commends 리스트를 만들어 놓고
    # 명령어의 3가지 종류인 I, D, A 를 담은 com_list 를 만들자
    commends = []
    com_list = ["I", "D", "A"]

    # 명령어들의 모임이 담긴 한 덩이의 리스트가 입력된다.
    input_list = list(input().split())

    # 명령어 묶음은 항상 명령어의 종류를 나타내는 알파벳이 맨 처음 등장하며
    # 다음 알파벳이 나오기 전까지가 명령어 묶음이 된다.
    # 따라서 각 명령어 종류 알파벳을 기준으로 분리하여 저장하자
    start_idx = 0
    for i in range(1, len(input_list)):
        if input_list[i] in com_list:
            commends.append(input_list[start_idx:i])
            start_idx = i
    print("#{}".format(test_case), end=" ")
    print(*secret_message(ori_se, commends))