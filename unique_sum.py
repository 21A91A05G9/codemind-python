n=int(input())
a=list(map(int,input().split()))[:n]
s=0
a=set(a)
for i in a:
    s+=i
print(s)