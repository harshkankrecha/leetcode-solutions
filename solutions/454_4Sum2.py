"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, 
return the number of tuples (i, j, k, l) such that:
0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
"""


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n=len(nums1)
        
        d={}
        for i in range(n):
            for j in range(n):
                s=-nums1[i]-nums2[j]
                d[s]=1+d.get(s,0)
        count=0
        for i in range(n):
            for j in range(n):
                s=nums3[i]+nums4[j]
                if d.get(s,False):
                    count+=d[s]
        return count
        