"""
You are given an array of integers nums, 
there is a sliding window of size k which is moving from 
the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.
Return the max sliding window.
"""



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        index=[float('inf')]*n
        
        stack=[n-1]
        
        for i in range(n-2,-1,-1):
            while len(stack)>0 and nums[stack[-1]]<nums[i]:
                stack.pop()
            
            if len(stack)>0:index[i]=stack[-1]
            stack.append(i)
        ans=[0]*(n-k+1)
        j=0
        for i in range(0,n-k+1):
            if j<i:j=i       
            while index[j]<i+k:
                j=index[j]
            
            ans[i]=nums[j]        
        return ans