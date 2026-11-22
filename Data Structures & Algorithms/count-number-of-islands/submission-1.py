class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0
        visit = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0' or (r,c) in visit:
                return
            visit.add((r,c))
            directions = [(1,0), (-1,0), (0,-1), (0,1)]

            for dx, dy in directions:
                dfs(r+dx, c+dy)
        

        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] != '0' and (i,j) not in visit:
                    count +=1
                    dfs(i, j)
        

        return count