class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        max_area = 0
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            area = 1
            while q:
                r,c = q.popleft()
                for dr, dc in dir:
                    if dr + r >= 0 and dc + c >= 0 and dc + c < COLS and dr + r < ROWS and grid[dr + r][dc + c] == 1:
                        grid[dr + r][dc + c] = 0
                        q.append((dr + r, dc + c))
                        area += 1
            return area
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    max_area = max(max_area, area)
                    
        return max_area