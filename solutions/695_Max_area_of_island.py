"""
You are given an m x n binary matrix grid. 
An island is a group of 1's (representing land) connected 
4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        visited=set()
        def dfs(i,j):
            if (i,j) not in visited:
                visited.add((i,j))
                moves=[(1,0),(-1,0),(0,1),(0,-1)]
                
                for di,dj in moves:
                    if 0<=i+di<=n-1 and 0<=j+dj<=m-1 and grid[i+di][j+dj]==1:
                        dfs(i+di,j+dj)
        
        mx=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and (i,j) not in visited:
                    prev=len(visited)
                    dfs(i,j)
                    cur=len(visited)
                    mx=max(mx,cur-prev)
        return mx