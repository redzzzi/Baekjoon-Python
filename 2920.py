# 2920 음계
ori = [k for k in range(1, 9)]
scale = []
for s in input().split():
    scale.append(int(s))
rescale = list(reversed(scale))

if ori == scale:
    print("ascending")
elif ori == rescale:
    print("descending")
else:
    print("mixed")

