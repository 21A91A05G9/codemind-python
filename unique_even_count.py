n=int(input())
a=list(map(int,input().split()))[:n]
s=0
a=set(a)
for i in a:
    if(i%2==0):
        s+=1
print(s)