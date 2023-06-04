# 3052 나머지
extra = []
while True:
    try:
        num = int(input())
        extra.append(num%42)
        if not num:
            break
    except: break
extra.sort()
org = list(set(extra))
print(len(org))
