n=int(input())
c=0
for i in range(0,n):
    s=input()
    c=0
    for j in range(0,len(s)):
        x=ord(s[j])-48
        for k in range(0,9):
            if(x==k):
                c+=1
    if(c==len(s)):
        print(True)
    else:
        print(False)