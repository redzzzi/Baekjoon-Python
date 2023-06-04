# 1157 단어 공부
word = list(input())
word = [x.upper() for x in word]
kind = list(set(word))
cnt = []
for i in kind:
    cnt.append(word.count(i))
maxnum = max(cnt)
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    final = kind[cnt.index(maxnum)]
    print(final)
i
