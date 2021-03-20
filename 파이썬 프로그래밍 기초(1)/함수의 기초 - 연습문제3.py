prime_judge = int(input())


def prime_judge_fn(t):
    yak_ct = 0
    for i in range(1,t+1):
        if t % i == 0:
            yak_ct += 1
    if yak_ct == 2:
        return '소수입니다.'
    else:
        return '소수가 아닙니다.'


print(prime_judge_fn(prime_judge))