class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0
        visit = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r,c) in visit:
                return 0
            result = 0
            visit.add((r,c))
            directions = [(1,0), (-1,0), (0,-1), (0,1)]

            for dx, dy in directions:
                result += dfs(r+dx, c+dy)
            
            return 1+result 
            
        

        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] != 0 and (i,j) not in visit:
                    res = dfs(i, j)
                    maxArea = max(maxArea, res)

        return maxArea
        