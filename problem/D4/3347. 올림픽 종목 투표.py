def solution(event, group):
    max_count = max_answer = 0
    answer = [0] * len(event)
    answer_dict = dict()

    for i in range(len(group)):
        if group[i] not in answer_dict.keys():
            for j in range(len(event)):
                if event[j] <= group[i]:
                    answer_dict[group[i]] = j
                    answer[j] += 1
                    if max_count < answer[j]:
                        max_count = answer[j]
                        max_answer = j
                    break
        else:
            answer[answer_dict[group[i]]] += 1
            if max_count < answer[answer_dict[group[i]]]:
                max_count = answer[answer_dict[group[i]]]
                max_answer = answer_dict[group[i]]

    return max_answer + 1


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print("#{} {}".format(test_case, solution(A, B)))
