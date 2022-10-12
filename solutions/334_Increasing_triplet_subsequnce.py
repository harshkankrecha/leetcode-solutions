"""
Given an integer array nums, return true if there exists 
a triple of indices (i, j, k) such that i < j < k and 
nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
"""

"""
TC = O(nlogn)
SC = O(n)
"""





import bisect
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        dp=[nums[0]]
        for i in range(1,len(nums)):
            idx=bisect.bisect_left(dp,nums[i])
            if idx==len(dp):
                dp.append(nums[i])
            else:
                dp[idx]=nums[i]
        return len(dp)>=3