scores = []

count = int(input("총 학생의 수를 입력하세요: "))

for i in range(1, count + 1):
    score = {}
    score['name'] = input("학생의 이름을 입력하세요: ")
    score['kor'] = int(input("{} 학생의 국어 점수를 입력하세요: ".format(score['name'])))
    score['mat'] = int(input("{} 학생의 수학 점수를 입력하세요: ".format(score['name'])))
    score['eng'] = int(input("{} 학생의 영어 점수를 입력하세요: ".format(score['name'])))
    scores.append(score)

for score in scores:
    total = 0
    for key in score:
        if key != 'name':
            total += score[key]
    print("{} => 총점: {}, 평균: {:.2F}".format(score['name'], total, total/3))

kor_total, mat_total, eng_total = 0, 0, 0
for score in scores:
    for key in score:
        if key == 'kor':
            kor_total += score[key]
        elif key == 'mat':
            mat_total += score[key]
        elif key == 'eng':
            eng_total += score[key]

print("국어 => 총점: {}, 평균: {}".format(kor_total, kor_total/len(scores)))
print("수학 => 총점: {}, 평균: {}".format(mat_total, mat_total/len(scores)))
print("영어 => 총점: {}, 평균: {}".format(eng_total, eng_total/len(scores)))