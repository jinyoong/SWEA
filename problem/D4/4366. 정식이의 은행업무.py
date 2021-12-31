def make_tri(binary, trinary):
    decimal = 0
    n = len(binary)

    for i in range(n-1, -1, -1):  # 2진수 10진수로
        decimal += binary[i] * 2 ** (n-1 - i)

    temp = []
    result = decimal

    while decimal > 2:  # 10진수 3진수로
        x, y = divmod(decimal, 3)
        temp = [y] + temp
        decimal = x
    temp = [decimal] + temp

    if len(temp) != len(trinary):  # 만든 3진수와 기억하고 있는 3진수의 자릿수가 다르면 => 추측할 수 없는 경우도 있을 수 있다
        return False, result

    cnt = 0
    for i in range(len(temp)):  # 3진수와 자리가 딱 하나 차이나는지 확인
        if temp[i] != trinary[i]:
            cnt += 1

    if cnt == 1:
        return True, result
    else:
        return False, result


def solution(binary, trinary):

    for i in range(len(binary)):  # 2진수 숫자를 한 자리씩 바꿔서 3진수로 만들어보기
        binary[i] = (binary[i] + 1) % 2
        ans = make_tri(binary, trinary)
        binary[i] = (binary[i] + 1) % 2
        if ans[0]:
            return ans[1]


T = int(input())

for test_case in range(1, T+1):
    binary = list(map(int, input()))
    trinary = list(map(int, input()))
    print('#{} {}'.format(test_case, solution(binary, trinary)))


######################################
# 유튜브 라이브

def change_to_dec(num, notation):  #notatin 진수 표현 숫자 num 을 10진수로 바꾸는 함수
    tmp = 0

    temp = list(map(int, num))[::-1]  # 문자열로 들어온 2진수를 뒤집힌 상태의 리스트로 만들기

    for n, val in enumerate(temp):
        tmp += val*(notation**n)

    return tmp


def check(num, notation):
    change_num = change_to_dec(num, notation)

    for n, val in enumerate(list(map(int, num))[::-1]):
        for j in range(notation):  # 한 비트씩만 바꾼 결과를 추가
            if val == j:
                continue
            tmp = change_num - val * (notation ** n) + j * (notation ** n)

            if tmp not in binary:
                binary.append(tmp)
            else:
                return tmp


def check2():
    bi_num = 0
    for x in bi:
        bi_num = bi_num * 2 + int(x)

    for i in range(len(bi)):
        binary.append(bi_num ^ (1 << i))
        # 1010 이면 0001, 0010, 0100 순으로 진행하면서
        # xor 연산을 하므로 1011, 1001, 1110 이 되게 된다. 즉, 한 비트씩만 바꾼 결과를 얻을 수 있다.

    for i in range(len(tr)):
        num1 = 0
        num2 = 0
        # 212 가 들어올 경우 num1: 012 / num2: 112 가 되도록 2개의 변수를 만들어 놓자
        for j in range(len(tr)):
            # i: 현재 바꾸고 싶은 자리 / j: 바꾸려고 하는 경우(2가지)
            if i != j:  # i 와 j 가 다르면 다음 자리로 넘어가야한다
                num1 = num1 * 3 + int(tr[j])
                num2 = num2 * 3 + int(tr[j])
            else:
                num1 = num1 * 3 + (int(tr[j]) + 1) % 3
                num2 = num2 * 3 + (int(tr[j]) + 2) % 3

        if num1 in binary:
            return num1
        if num2 in binary:
            return num2


T = int(input())

for test_case in range(1, T+1):
    bi = input()
    tr = input()

    binary = []

    check(bi, 2)
    # 2진수 숫자들을 한 비트씩 바꿔서 10진수로 바꿔 binary 에 저장!!
    # 여기서 check(tr, 3) 을 하면 binary 에 3진수 숫자 1개만 바꿨을 때 동일한 값이 나오는 경우를 반환하게 된다!

    print('#{} {}'.format(test_case, check(tr, 3)))
