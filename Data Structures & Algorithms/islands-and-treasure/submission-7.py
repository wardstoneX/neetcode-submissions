class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        visit = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:

                    visit.add((i,j))
                    q.append((i,j))    
            
       
        while q:
            qLen = len(q)
            for i in range(qLen):
                r,c = q.popleft()
                #visit.add((r,c))
                directions = [(1,0), (-1,0),(0,1), (0,-1)]

                for dx, dy in directions:
                    
                    # valid tile
                    if r+dx < ROWS and c+dy < COLS and r+dx >= 0 and c+dy >= 0:
                        if  grid[r+dx][c+dy] != -1 and (r+dx, c+dy) not in visit:
                            grid[r+dx][c+dy] = 1 + grid[r][c]
                            q.append((r+dx, c+dy))
                            visit.add((r+dx, c+dy))

        
        