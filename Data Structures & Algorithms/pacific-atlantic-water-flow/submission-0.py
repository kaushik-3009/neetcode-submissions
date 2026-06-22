class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = [[False]*COLS for _ in range(ROWS)], [[False]*COLS for _ in range(ROWS)]
        res = []
        pac_queue = deque()
        pac_visited = set()

        atl_queue = deque()
        atl_visited = set()

        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        

            


        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 and c==COLS-1:
                    pac_queue.append((r, c))
                    pac_visited.add((r, c))
                    atl_queue.append((r, c))
                    atl_visited.add((r, c))
                elif r == ROWS-1 and c == 0:
                    pac_queue.append((r, c))
                    pac_visited.add((r, c))
                    atl_queue.append((r, c))
                    atl_visited.add((r, c))
                elif r==0:
                    pac_queue.append((r, c))
                    pac_visited.add((r, c))
                elif c ==0:
                    pac_queue.append((r, c))
                    pac_visited.add((r, c))

                elif r==ROWS-1:
                    atl_queue.append((r, c))
                    atl_visited.add((r, c))
                elif c == COLS-1:
                    atl_queue.append((r, c))
                    atl_visited.add((r, c))
        print(pac_queue, atl_queue)
        while pac_queue:
            r, c = pac_queue.popleft()
            pac[r][c] = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0<=nr<ROWS and 0<=nc<COLS and heights[nr][nc] >= heights[r][c] and (nr, nc) not in pac_visited:
                    pac_queue.append((nr, nc))
                    pac_visited.add((nr, nc))
                    
    
        while atl_queue:
            (r, c) = atl_queue.popleft()
            atl[r][c] = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0<=nr<ROWS and 0<=nc<COLS and heights[nr][nc] >= heights[r][c] and (nr, nc) not in atl_visited:
                    atl_queue.append((nr, nc))
                    atl_visited.add((nr, nc))
                    
        
        print(pac)

        print(atl)
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] == True and atl[r][c] == True:
                    res.append([r, c])

        return res

# pac: (r, 0), (0, c)
# atl: (r, COLS-1), (ROWS-1, c)