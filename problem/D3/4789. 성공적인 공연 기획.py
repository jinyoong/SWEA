def applause(lst):
    clap_ct = 0  # 현재 박수치고 있는 사람의 수
    answer = 0  # 고용할 사람의 수
    for ele in lst:
        if int(ele[1]) == 0:  # 박수칠 사람이 없으면 다음 차례로
            continue

        if ele[0]-1 <= clap_ct:  # 현재 번호-1 이상으로 박수를 치고 있는 사람의 수가 있으면
            clap_ct += int(ele[1])  # 현재 번호의 사람들 모두 박수를 치므로 추가
            continue

        temp = ele[0]-1 - clap_ct  # 박수치는 사람이 부족하면 고용해야 한다
        clap_ct += (temp + int(ele[1]))  # 고용함과 동시에 해당 번호의 사람들 모두가 박수를 치고
        answer += temp  # 고용한 사람은 필요한 만큼만 추가
    return answer


T = int(input())

for test_case in range(1, T + 1):
    people = list(enumerate(input(), start=1))
    print("#{} {}".format(test_case, applause(people)))
