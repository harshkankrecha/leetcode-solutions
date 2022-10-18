"""
There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other 
cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if 
the ith city and the jth city are directly connected, 
and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.
"""



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        
        def dfs(src):
            if visited[src]==False:
                visited[src]=True
                
                for nbr in range(n):
                    if isConnected[src][nbr]==1:
                        dfs(nbr)
            
        count=0
        for i in range(n):
            if visited[i]==False:
                dfs(i)
                count+=1
        return count