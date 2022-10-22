"""
Given an unsorted integer array nums, 
return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) 
time and uses constant extra space.
TC: O(N)
SC: O(1)
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]<0:nums[i]=0
                
        for i in range(n):
            if nums[i]<0:
                if 0<=-nums[i]-1<=n-1:
                    if nums[-nums[i]-1]==0:
                        nums[-nums[i]-1]=-n-1
                        
                              
                    elif nums[-nums[i]-1]>0:
                        nums[-nums[i]-1]*=-1
                        
            elif nums[i]>0:
                if 0<=nums[i]-1<=n-1:
                    if nums[nums[i]-1]==0:
                        nums[nums[i]-1]=-n-1
                        
                    elif nums[nums[i]-1]>0:
                        nums[nums[i]-1]*=-1
                        
            
        
        for i in range(1,n+1):
            if nums[i-1]>=0:return i
        return n+1