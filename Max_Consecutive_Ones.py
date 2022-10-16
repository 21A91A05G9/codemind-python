n=int(input())
v=list(map(int,input().split()))
a,b=0,0
for k in v:
    if k==1:
        a+=1
    else:
        if a>b:
            b=a
        a=0
if a>b:
    b=a
print(b)