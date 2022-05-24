n=int(input())
b=[]
k=0
a=list(map(int,input().strip().split()))[:n]
for i in a:
    b.append(i*i)
for i in range(0,n-k):
    a[n-k-1]=max(b)
    k+=1
    b[b.index(max(b))]=0
for i in a:
    print(i,end=" ")
    