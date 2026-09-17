class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        def isisland(c, r):
            if c < 0 or c >= col:
                return 
            if r < 0 or r >= row:
                return 
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            isisland(c-1,r)
            isisland(c+1,r)
            isisland(c,r-1)
            isisland(c,r+1)

        for i in range(col):
            for j in range(row):
                if grid[j][i] == "1":
                    res += 1
                    isisland(i,j)
        return res
        
