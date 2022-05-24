n=int(input())
a=list(map(int,input().strip().split()))[:n]
for i in a:
    if(i==0):
        print(i,end=' ')
for j in a:
    if(j==1):
        print(j,end=' ')