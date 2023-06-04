# 1094 막대기

want = int(input())
bar = [64]

while sum(bar) > want:
    half = bar.pop(bar.index(min(bar)))//2
    bar.append(half)
    bar.append(half)
    if sum(bar)-half >= want:
        bar.pop(bar.index(half))
    else: continue

print(len(bar))
