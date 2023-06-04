case_num = int(input())
data = {}
for i in range(case_num):
    case = list(map(int,input().split()))
    data[i] = case
for j in range(case_num):
    avg = sum(data[j][1:])/data[j][0]
    hi = [k for k in data[j][1:] if k > avg]
    ra = (len(hi)/(len(data[j])-1))*100
    print(f"{ra:.3f}%")
