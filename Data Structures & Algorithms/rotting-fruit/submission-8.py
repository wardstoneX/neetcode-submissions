class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = collections.deque()
        result = 0
        freshFruits = 0
        directions = [(1,0), (-1,0), (0,1),(0,-1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    freshFruits +=1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        while q and freshFruits > 0:
            
            #print(q, freshFruits)
            lenQ = len(q)
            result+=1
            for i in range(lenQ):
                r,c = q.popleft()
                for dx, dy in directions:
                    if not (r + dx < 0 or c+dy < 0 or r + dx >= ROWS or c+dy >= COLS):
                        if grid[r+dx][c+dy] == 1:
                            grid[r+dx][c+dy] = 2
                            freshFruits -=1
                            q.append((r+dx, c+dy))
                
        
        
        return result if freshFruits == 0 else -1

        