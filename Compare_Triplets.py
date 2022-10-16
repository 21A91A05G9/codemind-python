v=list(map(int,input().split()))
k=list(map(int,input().split()))
j=l=0
for i in range(3):
    if v[i]>k[i]:
        j+=1
    elif v[i]<k[i]:
        l+=1
print(j,l)