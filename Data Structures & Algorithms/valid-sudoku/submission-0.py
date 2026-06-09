class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_map = [set() for i in range(9)]
        col_map = [set() for i in range(9)]
        box_map = [set() for i in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                box_idx = r//3*3 + c//3
                if board[r][c] in row_map[r] or board[r][c] in col_map[c] or board[r][c] in box_map[box_idx]:
                    return False
                row_map[r].add(board[r][c])
                col_map[c].add(board[r][c])
                box_map[box_idx].add(board[r][c])

        return True

# 0-3, 3, 7, 7, 10

# r, c

# # for every row, that col should have no dupicates, so you add nums to has table and check?
# # for every col you keep separate hash table
# # 

# r, c: 0-3

# # 3 diff hashtable?


# 0, 9
# 0, 9

# 0-3, 0-3 // 3-6,0-3