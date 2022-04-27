t=int(input())
for j in range(1,t+1):
    c=0
    n,m=input().split()
    n=int(n)
    m=int(m)
    for i in range(n,m+1):
        d=i%10
        if(d==2 or d==3 or d==9):
            c+=1
        i+=1
    print(c)   