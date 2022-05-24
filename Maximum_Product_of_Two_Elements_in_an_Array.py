a=list(map(int,input().strip().split()))
max=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if((a[i]-1)*(a[j]-1)>max):
            max=(a[i]-1)*(a[j]-1)
print(max)