n=int(input())
k=0
a=list(map(int,input().strip().split()))[:n]
for i in a:
    k=0
    for j in a:
        if(j<i):
            k+=1
    print(k,end=' ')
    