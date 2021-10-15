import sys

sys.stdin = open('1244.txt')


def solution(number, idx, n):
    if idx >= len(number)-1:  # 교체 횟수를 다 쓰기 전에 끝까지 바꾼 경우
        if n % 2:  # 홀수번 남아있는 경우
            number[-1], number[-2] = number[-2], number[-1]
        new_num = ''.join(map(str, number))
        result.append(int(new_num))
        return

    if n == 0:  # 교체 횟수를 다 쓴 경우
        new_num = ''.join(map(str, number))  # 현재 숫자 추가
        result.append(int(new_num))
        return

    temp = number[idx+1:]
    max_num = max(temp)
    if number[idx] >= max_num:  # 만약 현재 숫자보다 큰 수가 뒤에 없다면
        solution(number, idx+1, n)  # 교체 횟수 늘리지 않고 다음 인덱스로

    for i in range(len(number) - 1, idx, -1):
        if number[i] != max_num:
            continue
        number[idx], number[i] = number[i], number[idx]
        solution(number, idx + 1, n - 1)
        if temp.count(max_num) == 1:  # 만약 idx 번째 수보다 큰 수가 1개라면 1가지 경우만 있다
            continue
        number[idx], number[i] = number[i], number[idx]


T = int(input())

for test_case in range(1, T+1):
    number_str, n = input().split()
    number_lst = list(map(int, number_str))
    result = []
    idx = 0
    solution(number_lst, idx, int(n))
    print("#{} {}".format(test_case, max(result)))


# def change2(number, cnt):
#     length = len(number)
#     number = list(map(int, number))
#     goal_number = sorted(number, reverse=True)
#
#     need_cnt = 0
#     for i in range(length):
#         if number[i] != goal_number[i]:
#             need_cnt += 1
#     need_cnt /= 2
#
#     if need_cnt % 1 == 0:
#         need_cnt = int(need_cnt)
#     else:
#         need_cnt = int(need_cnt) + 1
#
#     if need_cnt == cnt:
#         result = goal_number
#     elif need_cnt > cnt:  # 제일 큰 수로 만드는데 필요한 교환 횟수보다 주어진 횟수가 더 적은 경우
#         result = change(number, cnt)
#     else:
#         if number.count(max(number)) >= 2:
#             pass
#         else:
#             goal_number[-2], goal_number[-1] = goal_number[-1], goal_number[-2]
#         result = goal_number
#
#     return ''.join(map(str, result))
#
#
# def change(number, cnt):
#     length = len(number)
#     number = list(map(int, number))
#     goal_number = sorted(number, reverse=True)
#     change = 0
#     start_idx = 0
#     while change != cnt:
#         # if start_idx >= length or number == goal_number:
#         #     if number[0] == number[1]:
#         #         pass
#         #     else:
#         #         number[-1], number[-2] = number[-2], number[-1]
#         #     return ''.join(map(str, number))
#
#         if number[start_idx] == goal_number[start_idx]:
#             start_idx += 1
#             continue
#         min_num = min(number)
#         min_idx = number.index(min_num)
#         if min_idx < cnt:
#             temp = min_idx
#         else:
#             temp = start_idx
#             start_idx += 1
#         max_num = max(number[temp:])
#         max_idx = temp
#         for i in range(length-1, temp, -1):
#             if number[i] == max_num:
#                 max_idx = i
#                 break
#         number[temp], number[max_idx] = number[max_idx], number[temp]
#         change += 1
#
#     return number
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     number, n = input().split()
#     cnt = int(n)
#     print(f'#{test_case} {change2(number, cnt)}')