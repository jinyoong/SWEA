def mean_score(numbers):
    score_sum = 0
    score_ct = 0
    for number in numbers:
        if number <= 40:
            number = 40
        score_sum += number
        score_ct += 1
    return score_sum // score_ct

T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    print("#{} {}".format(test_case, mean_score(numbers)))
