for i in range(int(input())):
    n=int(input())
    v=list(map(int,input().split()))
    k=sorted(v)
    if v==k:
        print(0)
    else:
        print(k[-1]-k[0])