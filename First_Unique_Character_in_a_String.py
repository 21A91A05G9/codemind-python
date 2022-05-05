s=(input())
c=1
for i in range(0,len(s)):
    c=1
    for j in range(0,len(s)):
        if(s[i]==s[j] and i!=j):
            c=0
            break
    if(c==1):
        print(i)
        break
else:
    print("-1")