s=input()
s=list(s.split())
for i in range(len(s)-1,-1,-1):
    for j in s[i]:
        print(j)
        break
    break
