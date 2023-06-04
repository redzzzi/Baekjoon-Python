# 2675 문자열 반복
T = int(input())
result = []
for _ in range(T):
    word = []
    R, S = input().split()
    lstS = list(S)
    for i in range(len(lstS)):
        plus = lstS[i]*int(R)
        word.append(plus)
    fiword = "".join(word)
    result.append(fiword)
for j in result:
    print(j)
