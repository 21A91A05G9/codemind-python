n=int(input())
a=list(map(int,input().strip().split()))[:n]
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i,end=' ')