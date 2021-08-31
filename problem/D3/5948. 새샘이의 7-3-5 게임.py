def number_sort(number_list):
    for i in range(5):
        max_idx = i
        for j in range(i, len(number_list)):
            if number_list[j] > number_list[max_idx]:
                max_idx = j
        number_list[i], number_list[max_idx] = number_list[max_idx], number_list[i]
    return number_list[4]


def number_sum(numbers, idx, ct, num_sum):
    global result

    if idx > len(numbers):
        return

    if ct == 3:
        if num_sum not in result:
            result.append(num_sum)
        return

    for i in range(idx, len(numbers)):
        number_sum(numbers, i+1, ct+1, num_sum+numbers[i])

    return result


T = int(input())

for test_case in range(1, T + 1):
    input_list = list(set(map(int, input().split())))
    result = []
    numbers2 = number_sum(input_list, 0, 0, 0)
    answer = number_sort(numbers2)
    print('#{} {}'.format(test_case, answer))
