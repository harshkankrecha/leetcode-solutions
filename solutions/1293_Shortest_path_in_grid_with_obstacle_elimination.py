"""
You are given an m x n integer matrix grid where each cell is 
either 0 (empty) or 1 (obstacle). 
You can move up, down, left, or right from and to an empty cell in one step.
Return the minimum number of steps to walk from the upper left corner (0, 0) 
to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles.
If it is not possible to find such walk return -1.
"""



class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:        
        n=len(grid)
        m=len(grid[0])
        
        if k>=n+m-2:return n+m-2
        q=[(0,0,0,k)]
        
        visited=set()
        visited.add((0,0,0,k))
        dirs=[(0,1),(0,-1),(-1,0),(1,0)]
        
        while len(q)>0:
            count,i,j,rem=q.pop(0)
            
            if (i,j)==(n-1,m-1):return count
            
            for di,dj in dirs:
                if 0<=i+di<n and 0<=j+dj<m:
                    nrem=rem-grid[i+di][j+dj]
                    
                    if nrem>=0 and (i+di,j+dj,nrem) not in visited:
                        visited.add((i+di,j+dj,nrem))
                        
                        q.append((1+count,i+di,j+dj,nrem))
        return -1