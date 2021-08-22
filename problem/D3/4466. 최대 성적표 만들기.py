def make_max_score(n, k, scores):
    # 0 ~ 100 까지의 점수가 들어오니까
    # 카운팅 정렬을 해서 오름차순으로 정렬을 해주자
    temp = [0] * 101
    for score in scores:
        temp[score] += 1

    for i in range(1, 101):
        temp[i] += temp[i-1]
    result = [0] * (n + 1)

    for i in range(-1, -(n + 1), -1):
        result[temp[scores[i]]] = scores[i]
        temp[scores[i]] -= 1

    # 오름차순으로 정렬된 리스트에서
    # 뒤에서부터 k 개의 숫자를 더해주자
    max_score = 0
    for i in range(-1, -(k + 1), -1):
        max_score += result[i]
    return max_score


T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    print("#{} {}".format(test_case, make_max_score(n, k, scores)))
