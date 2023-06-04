# 1120 / 문자열 / ╰（‵□′）╯

A, B = input().split()

diff = 0
if len(A) == len(B):
    for i, j in zip(A, B):
        if i != j:
            diff += 1
    print(diff)
else:
    while len(A) != len(B):
        


# 끝 - ! / o(*^▽^*)┛
