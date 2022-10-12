n=int(input())
l=list(map(int,input().split()))[:n]
k=int(input())
s=0
for i in l:
    s+=i
    if(i==k):
        break
print(s)