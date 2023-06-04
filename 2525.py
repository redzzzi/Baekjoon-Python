# 2525 오븐 시계
h, m = map(int,input().split())
time = int(input())
m += time
if m >= 60:
    a = m//60
    m -= 60*a
    h += 1*a
    if h >= 24:
        h -= 24
    print(f"{h} {m}")
else: print(f"{h} {m}")
