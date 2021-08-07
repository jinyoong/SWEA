def tree(string_in):
    boonja = 1
    boonmo = 1
    for alpha in string_in:
        if alpha == 'L':
            boonmo += boonja
        else:
            boonja += boonmo
    return boonja, boonmo

T = int(input())

for test_case in range(1, T+1):
    alphas = input()
    print(f'#{test_case} {tree(alphas)[0]} {tree(alphas)[1]}')