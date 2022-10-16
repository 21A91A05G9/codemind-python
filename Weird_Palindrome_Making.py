for i in range(int(input())):
    i=int(input())
    v=list(map(int,input().split()))
    k=0
    for r in v:
        k+=(r%2)
    print(k//2)