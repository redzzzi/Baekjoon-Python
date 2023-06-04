total = int(input())

numlst = []
for _ in range(total):
    num = int(input())
    numlst.append(num)

numlst2 = list(set(numlst))
numlst2.sort()

for i in numlst2:
    print(i)
