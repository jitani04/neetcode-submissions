class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0
        
        def bfs(row, col):
            q = deque()
            q.append((row,col))
            grid[row][col] = '0'
            dir = [(0, 1), (0,-1), (1, 0), (-1, 0)]
            
            while q:
                r, c = q.popleft()
                for v, h in dir:
                    if r + v < ROWS and c + h < COLS and c + h >= 0 and r + v >= 0:
                        if grid[r + v][c+ h] == '1':
                            q.append((r + v, c + h))
                            grid[r + v][c + h] = '0'

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    num_islands += 1
                    bfs(row,col)
        return num_islands
