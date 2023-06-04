# 8958 OX퀴즈
n = int(input())
scr = []
for _ in range(n):
    score = 0
    plus = 1
    typing = input()
    game = [k for k in typing]
    for i in game:
        if i == "O":
            score += plus
            plus += 1
        else:
            plus = 1
    scr.append(score)
for j in scr:
    print(j)
