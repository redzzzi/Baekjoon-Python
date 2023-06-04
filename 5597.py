# 5597 과제 안 내신 분..?
submit = []
while True:
    try:
        stud = int(input())
        submit.append(stud)
        if not stud:
            break
    except: break
xsubmit = []
for i in range(1,31):
    if i in submit:
        continue
    else: xsubmit.append(i)
xsubmit.sort()
for j in xsubmit:
    print(j)
