n=int(input())
l=list(map(int,input().split()))[:n]
if l.count(0)+l.count(1)==len(l):
    print(True)
else:
    print(False)
    