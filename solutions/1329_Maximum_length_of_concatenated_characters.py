"""
You are given an array of strings arr. A string s is formed by the 
concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or 
no elements without changing the order of the remaining elements.
"""

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def isvalid(s):
            st=set()
            for x in s:
                st.add(x)
            return len(st)==len(s)
        
        mx=0
        def helper(i,s):
            nonlocal mx            
            if i>=len(arr):
                if isvalid(s):
                    mx=max(mx,len(s))
                return
            
            helper(i+1,s+arr[i])
            helper(i+1,s)
            
        helper(0,'')
        return mx