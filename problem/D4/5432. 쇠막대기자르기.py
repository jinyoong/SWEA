import sys

sys.stdin = open("input.txt")


def cut_pipe(pipe):
    idx = 0

    # result : 레이저로 인해 잘려지는 쇠막대기의 총 개수
    # piece_ct : 레이저를 만나기 전까지 겹쳐져 있는 쇠막대기의 개수
    result = 0
    piece_ct = 0

    # 쇠막대기가 겹쳐질 수 있는데 겹쳐진 상태에서 레이저에 맞으면 겹쳐진 만큼 조각이 발생한다
    # 중요한 것은 겹쳐진 쇠막대기의 맨 위의 쇠막대는 레이저에 맞지 않더라도
    # 쇠막대의 길이가 끝나면 레이저로 조각이 난 것처럼 한 조각을 남기고 사라진다
    while idx < len(pipe) :
        # print("현재 겹쳐진 쇠막대기 : {}".format(piece_ct))

        # 레이저는 () 형태이므로 이 괄호 모양이 나오는지 우선적으로 확인하자
        # 만약 레이저가 나오게 되면 그 전에 쌓여있던 쇠막대기를 모두 자르므로
        # 겹친 만큼의 조각이 나오게 된다
        if idx <= len(pipe) - 2 and pipe[idx:idx+2] == '()':
            idx += 2
            # print("레이저로 인해 생기는 조각: {}, 전체 조각 수: {}".format(piece_ct, result))
            result += piece_ct

        # 괄호의 모양이 ( 라는 것은 쇠막대기가 겹치기 시작한다는 의미이므로
        # 겹쳐진 양을 1 늘려준다
        elif pipe[idx] == "(":
            idx += 1
            piece_ct += 1

        # 괄호의 모양이 ) 라는 것은 쇠막대기의 끝까지 도달했다는 뜻이 된다
        # 레이저 이후로 ) 모양이 나오기 전까지의 부분이 1조각이 되서 떨어지게 되므로
        # 겹쳐진 양을 1 줄이고, 전체 조각 수에 1을 더해주자
        elif pipe[idx] == ")":
            idx += 1
            piece_ct -= 1
            result += 1

    return result


T = int(input())

for test_case in range(1, T + 1):
    input_str = input()
    print("#{} {}".format(test_case, cut_pipe(input_str)))

