# 1032 명령 프롬프트
N = int(input())
files = []
for _ in range(N):
    file = list(input())
    files.append(file)
common = files[0]
for i in range(N-1):
    for j in range(len(files[0])):
        if files[i][j] == files[i+1][j]:
            continue
        else: common[j] = "?"
print("".join(common))
