# 1334 / 다음 팰린드롬 수 / ╰（‵□′）╯

N = input()
leN = len(N)

if N == "9"*leN:
    print(int(N)+2)
elif 1 <= int(N) < 9:
    print(int(N)+1)
elif leN%2 == 0:
    plus = N[:leN//2]
    new = plus + plus[::-1]
    if int(N) < int(new):
        print(int(new))
    else:
        plus = str(int(plus)+1)
        new = plus + plus[::-1]
        print(int(new))
else:
    plus1 = N[:leN//2]
    plus2 = N[:leN//2+1]
    new = plus2 + plus1[::-1]
    if int(N) < int(new):
        print(int(new))
    else:
        plus2 = str(int(plus2)+1)
        plus1 = plus2[0:len(plus2)-1]
        new = plus2 + plus1[::-1]
        print(int(new))

# 통과 통과 통과 통과
