n=int(input())
l=list(map(int,input().split()))[:n]
j,s=0,0
for i in range(len(l)-1,-1,-1):
    s+=l[i]*(2**j)
    j+=1
print(s) 