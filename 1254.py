class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:


        rows=len(grid)
        cols=len(grid[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols:
                return False

            if grid[i][j]==1:
                return True
            grid[i][j]=1

            a=dfs(i+1,j)
            b=dfs(i-1,j)
            c=dfs(i,j+1) 
            d=dfs(i,j-1)

            return a and b and c and d

        count=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    if dfs(i,j):
                        count+=1
        return count       




