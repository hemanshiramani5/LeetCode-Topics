class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums) #3
        asc=1
        dsc=1

        for i in range(1,n):
            if nums[i]==(nums[i-1]+1)%n: #2==2-1+1%3=2  2==2
                asc+=1   #3
            if nums[i-1]==(nums[i]+1)%n:  #2-1=2==2+1%3=0  1=2
                dsc+=1  

        if asc==n:  #2==2
           if nums[0]==0: 
            return 0    
           return min(n-nums[0],nums[0]+2)   2-0,0+2

        if dsc==n:
            return min(n-nums[-1],nums[-1])+1
        return -1    



        