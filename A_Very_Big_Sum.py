n = int(input())
s=0
a = list(map(int,input().strip().split()))[:n]
for i in a:
    s+=i
print(s)