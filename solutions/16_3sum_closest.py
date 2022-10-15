"""
Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.


"""



import bisect
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mnd=ans=float('inf')
        
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                s=nums[i]+nums[j]
                idx=bisect.bisect_right(nums[j+1:],target-s)
                if idx==0:
                    if nums[j+1]-target+s<mnd:
                        mnd = nums[j+1]-target+s
                        ans=s+nums[j+1]
                        
                elif idx==len(nums[j+1:]):
                    if target-s-nums[-1]<mnd:
                        mnd = target-s-nums[-1]
                        ans=s+nums[-1]
                        
                else:
                    diff1=target-s-nums[j+1:][idx-1]
                    if diff1<mnd:
                        mnd=diff1
                        ans=s+nums[j+1:][idx-1]
                    diff2=nums[j+1:][idx]-target+s
                    if diff2<mnd:
                        mnd=diff2
                        ans=s+nums[j+1:][idx]
        return ans