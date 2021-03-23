data_str = "파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다."

mask_str = input('마스킹할 문자열을 입력하세요: ')

find_str = input('찾을 문자열을 입력하세요: ')

idx = -1
count = 1
while True:
    idx = data_str.find(find_str, idx + 1)
    # find와 rfind 모두 두 번째 인자로 시작 인덱스를 설정해 줄 수 있따.
    if idx != -1:
        print('[{}] ~ [{}]'.format(idx, idx + len(find_str) - 1))
        # 우리가 찾는 것은 '객체'라는 문자열이기 때문에 시작 인덱스부터 그 다음 인덱스까지에 해당한다.
        new_str = data_str.replace(find_str, mask_str, count)
        # replace 함수는 세 번째 인자로 교체를 몇 번 할지 정할 수 있다.
        print(new_str)
        count += 1
    else:
        break