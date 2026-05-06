from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        seen = set()

        def dfs(r, c):
            q = deque()
            seen.add(grid[r][c])
            q.append((r, c))

            while q:
                row, col = q.pop() #popleft for bfs
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in seen and grid[nr][nc] == '1'):
                        q.append((nr, nc))
                        seen.add((nr, nc))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in seen:
                    dfs(row, col)
                    islands += 1
        return islands         