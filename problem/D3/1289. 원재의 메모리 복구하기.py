def memory_restore(bit_list):
    """
    :param bit_list: 0 비트를 해당 비트 리스트와 똑같이 만들어야 한다.
    :return: 똑같이 만드는데 필요한 최소 횟수
    먼저 1 과 0 값 중 하나를 선택해 어떠한 위치에 넣으면
    그 값으로 그 뒤의 모든 비트가 변경된다
    즉, 앞에서부터 변경하기 시작해보자
    """
    initial_list = [0] * len(bit_list)
    change_ct = 0
    for i in range(len(bit_list)):
        if initial_list[i] == bit_list[i]:
            pass
        else:
            for j in range(i, len(bit_list)):
                initial_list[j] = bit_list[i]
            change_ct += 1
    return change_ct

T = int(input())

for test_case in range(1, T + 1):
    bit_list = list(map(int, input()))
    print("#{} {}".format(test_case, memory_restore(bit_list)))