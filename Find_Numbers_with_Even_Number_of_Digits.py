n=int(input())
k=0
a=list(map(int,input().strip().split()))[:n]
for i in a:
    if (len(str(i)))%2==0:
        k+=1
print(k)
    