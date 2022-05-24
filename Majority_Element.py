n=int(input())
max=0
a=list(map(int,input().strip().split()))[:n]
for i in a:
    if(a.count(i)>max):
        max=a.count(i)
        x=i
print(x)