def cipher_code(garo, ciphers):
    # 각 행을 보며 0으로만 이루어진 문자열이 아닌지 확인하자
    # 암호코드가 속한 행을 찾았으면 이제 암호코드만을 추출해야 한다
    # 앞에서부터 판단하면 0 이 의미없는 0 인지, 숫자를 구성하는 0 인지 알 수가 없다
    # 모든 숫자 코드의 맨 끝은 1 인 것을 이용해야 한다
    # 즉, 끝에서부터 하나씩 보면서 처음으로 1이 나온 순간부터 56개의 코드를 살펴봐야 한다
    in_code = ''
    for cipher in ciphers:
        if cipher != '0' * garo:
            in_code = cipher
    for i in range(garo-1, -1, -1):
        # 암호 코드가 들어있는 행의 맨 끝에서부터 처음으로 1이 나오는 인덱스를 찾자
        if in_code[i] == '1':
            # 1이 처음으로 나온 순간부터 56 개의 문자들이 암호를 구성하는 문자이다
            # 만약 1이 60 번째 인덱스에서 처음 나왔다면
            # 암호의 시작은 60 부터 55번째 앞에 있는 5 인덱스가 암호의 시작 인덱스가 된다.
            code = [''] * 8
            ct = 0
            idx = 0
            for j in range(55, -1, -1):
                # 따라서 암호의 맨 처음은 i - 55 가 되며, 암호의 맨 끝은 i - 0 인덱스가 된다
                # 암호를 구성하는 숫자는 7개의 문자들로 구성되어 있으므로
                # 이어 붙인 수가 7의 배수를 넘어갈때마다 그 다음 숫자가 되게끔 하자
                code[idx] += in_code[i-j]
                ct += 1
                idx = ct//7
            break

    secret_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
                   '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

    result = []

    # 각 자리의 암호 숫자들을 숫자들로 변환한다
    for code_element in code:
        result.append(secret_dict[code_element])

    # 변환한 숫자들로 올바른 암호코드인지 확인하자
    # 올바른 암호코드 규칙에 맞게 저장할 변수로 is_code 를 초기화 하고
    # 올바른 암호코드일 시 전체 합을 출력해야 하니까 code_sum 을 초기화 하자
    is_code = 0
    code_sum = 0
    for i in range(8):
        if (i + 1) % 2:
            is_code += result[i] * 3
            code_sum += result[i]
        else:
            is_code += result[i]
            code_sum += result[i]

    if is_code % 10 == 0:
        return code_sum
    else:
        return 0


T = int(input())

for test_case in range(1, T + 1):
    sero, garo = map(int, input().split())
    ciphers = [input() for _ in range(sero)]
    print("#{} {}".format(test_case, cipher_code(garo, ciphers)))
