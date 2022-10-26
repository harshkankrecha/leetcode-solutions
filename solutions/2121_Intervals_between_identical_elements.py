"""
You are given a 0-indexed array of n integers arr.
The interval between two elements in arr is defined as the absolute 
difference between their indices. More formally, 
the interval between arr[i] and arr[j] is |i - j|.
Return an array intervals of length n where intervals[i] is 
the sum of intervals between arr[i] and each element in arr 
with the same value as arr[i].
Note: |x| is the absolute value of x
"""

from collections import deque
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        def helper(a):
            
            psum=[0]
            ssum=deque([0])

            for i in range(0,len(a)-1):
                psum.append(psum[-1]+a[i])
            for i in range(len(a)-1,0,-1):
                ssum.appendleft(ssum[0]+a[i])
            return (psum,ssum)
        ans=[0]*len(arr)        
        d=defaultdict(list)
        
        for i in range(len(arr)):
            d[arr[i]].append(i)
        #print(d)
        for x in d:
            psum,ssum=helper(d[x])
            #print(psum,ssum)
            for i in range(len(d[x])):
                ans[d[x][i]]=i*d[x][i]-psum[i]+ssum[i]-(len(d[x])-i-1)*d[x][i]
        return ans