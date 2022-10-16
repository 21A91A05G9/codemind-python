for i in range(int(input())):
    n,k=map(int,input().split())
    v=list(map(int,input().split()))
    r=[]
    k=k%n
    for j in range(n):
        if j>=k:
            r.append(v[j-k])
        else:
            r.append(v[n+j-k])
    print(*r)