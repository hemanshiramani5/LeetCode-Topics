class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps=0 
        curr_end=0
        fast=0
        
        for i in range(len(nums)-1):
            fast=max(fast,i+nums[i])

            if i==curr_end:
                jumps+=1
                curr_end=fast
        return jumps        
