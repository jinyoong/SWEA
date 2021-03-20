name1 = input()
name2 = input()
hand_name1 = input()
hand_name2 = input()

def 가위바위보(hand_name1, hand_name2):
    if hand_name1 == '가위':
        if hand_name2 == '바위':
            return "바위가 이겼습니다!"



print(가위바위보(hand_name1, hand_name2))
