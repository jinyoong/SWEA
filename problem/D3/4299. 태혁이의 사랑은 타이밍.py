def calc_time(day, hour, minute):
    standard = 60 * 24 * 11 + 60 * 11 + 11
    wait_time = 60 * 24 * day + 60 * hour + minute
    if standard <= wait_time:
        return wait_time - standard
    else:
        return -1


T = int(input())

for test_case in range(1, T + 1):
    d, h, m = map(int, input().split())
    print('#{} {}'.format(test_case, calc_time(d, h, m)))

"""
T=int(input())
for t in range(T):
    d,h,m=map(int,input().split())
    if(d<11) : 
        print("#%d -1" %(t+1))
    if(d==11 and ((h < 11)or(h==11 and m<11))):
        print("#%d -1" %(t+1))
    else:
        a = (d-11)*24*60+(h-11)*60+m-11
        print("#%d %d" %(t+1, a))
"""
