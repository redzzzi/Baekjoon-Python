# 1181 단어 정렬
N = int(input())
lst = []
for _ in range(N):
    tp = str(input())
    lst.append(tp)
fin = list(set(lst))
fin.sort()
fin.sort(key=len)
for j in fin:
    print(j)


