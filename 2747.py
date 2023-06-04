#피보나치 수
order = int(input())
fib = [0, 1]
for j in range(2,order+1):
    fib.append(fib[j-2]+fib[j-1])
print(fib[order])
