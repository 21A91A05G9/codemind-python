n=int(input())
a=list(map(int,input().split()))[:n]
s=0
for i in a:
    while(i):
        s+=i%10
        i//=10
print(s)