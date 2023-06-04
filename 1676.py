# 1676 팩토리얼 0의 개수 (✿◕‿◕✿)

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return(result)

N = int(input())

lst = list(str(factorial(N)))
numlst = [int(x) for x in lst]

numlst.reverse()

cnt = 0
for i in range(len(numlst)):
    if numlst[i] == 0:
        cnt += 1
    else:
        break
print(cnt)

