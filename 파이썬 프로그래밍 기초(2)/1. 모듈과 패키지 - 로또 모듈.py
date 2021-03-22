# random 함수 사용시

import random

'''lotto = random.sample(range(1, 46, 1), 6)
# sample() 함수는 리스트에서 주어진 인자의 수 만큼 비복원 추출한다.
print(sorted(lotto))'''


# 사용자 지정 모듈 사용시

def input_start():
    # 번호의 시작값을 받아올 함수를 생성
    # 이 때 입력값이 숫자가 아닐 경우를 대비하여 try except finally를 이용하여 예외처리를 한다.
    start = 0
    try:
        start = int(input("로또 번호의 시작 번호를 입력하세요 (기본값: 1): "))
    except:
        start = 1
    finally:
        return start

def input_end():
    end = 0
    try:
        end = int(input("로또 번호의 끝 번호를 입력하세요 (기본값: 45): "))
    except:
        end = 45
    finally:
        return end

def input_count():
    count = 0
    try:
        count = int(input("로또 공의 개수를 입력하세요 (기본값: 6): "))
    except:
        count = 6
    finally:
        return count

def print_lotto(start, end, count):
    lotto = random.sample(range(start, end + 1), count)
    print("행운의 로또 번호는 ", end="")
    # 크기 순서대로 나열하기 위해 enumerate()함수를 사용한다.
    # i는 인덱스, num은 로또 공의 숫자인데, i가 만약 lotto 리스트의 맨 마지막 인덱스라면
    # ,가 뒤에 붙을 필요가 없으므로 아래처럼 if 문으로 나누어 진행한다.
    for i, num in enumerate(sorted(lotto)):
        if i == len(lotto) - 1:
            print("{} ".format(num), end="")
        else:
            print("{}, ".format(num), end="")
    print("입니다.")


#print_lotto(1, 45, 6)