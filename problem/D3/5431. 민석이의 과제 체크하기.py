def check(n, students):
    checked_stu = [0] * (n + 1)
    checked_stu[0] = 1
    result = []
    for student in students:
        checked_stu[student] = 1
    for i in range(n+1):
        if checked_stu[i] == 0:
            result.append(i)
    return result


T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    students = list(map(int, input().split()))
    print("#{}".format(test_case), *check(n, students))
