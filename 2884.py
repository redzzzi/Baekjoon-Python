#2884 알람 시계
h, m = map(int,input().split())

if m < 45:
    h -= 1
    if h < 0:
        h += 24
    m += 15
    print(f"{h} {m}")
else: print(f"{h} {m-45}")    
