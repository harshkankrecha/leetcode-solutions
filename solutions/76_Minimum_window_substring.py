"""
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t 
(including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.
"""





import heapq
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        if m>n:return ""
        q=[]
        d={}
        for x in t:
            d[x]=[]
        
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]].append(i)
        
        left,right=-1,-1
        ml=float('inf')
        mx=0
        for x in t:
            if len(d[x])==0:return ""
            heapq.heappush(q,(d[x][0],x))
            mx=max(mx,d[x][0])
            d[x].pop(0)            
        
        while len(q)>0:
            val,x=heapq.heappop(q)
            if mx-val<ml:
                ml=mx-val
                left,right=val,mx
            if len(d[x])==0:
                break
            heapq.heappush(q,(d[x][0],x))
            mx=max(mx,d[x][0])
            d[x].pop(0)
            
        if left!=-1 and right!=-1:
            return s[left:right+1]
        return ""