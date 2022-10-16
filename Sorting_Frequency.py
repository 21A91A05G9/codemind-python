def solve(nums):
   dic={}
   for i in set(nums):
        x=nums.count(i)
        try:
            dic[x].append(i)
        except:
            dic[x]=[i]
   ans=[]
   for i in sorted(dic):
      for j in sorted(dic[i],reverse=True):
         ans.extend([j]*i)
   return ans[::-1]
n=int(input())
nums=solve(list(map(int,input().split())))
vk=[]
for r in nums:
    if r not in vk:
        vk.append(r)
print(*vk,sep=' ')