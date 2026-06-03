class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(r, c):
            if r == m-1 and c==n-1:
                return grid[r][c]
            
            if r>=m or c>=n:
                return 99999999999999999
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            down_path = dfs(r+1, c)
            right_path = dfs(r, c+1)

            memo[(r, c)] = grid[r][c] + min(down_path, right_path)

            return memo[(r,c)]
            
        

        return dfs(0, 0)