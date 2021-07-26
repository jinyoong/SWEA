def pattern(string_in):
    for i in range(2, len(string_in)//2 + 1):
        if string_in[:i] == string_in[i:2 * i]:
            return i

T = int(input())

for test_case in range(1, T + 1):
    case = input()
    print(f'#{test_case} {pattern(case)}')