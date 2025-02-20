class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = {}
            for char in row:
                if char in seen:
                    return False
                elif char != '.':
                    seen[char] = 1
        for col_id in range(9):
            col = [row[col_id] for row in board]
            seen = {}
            for char in col:
                if char in seen:
                    return False
                elif char != '.':
                    seen[char] = 1
        for x_qdrant in range(3):
            for y_qdrant in range(3):
                subbox = []
                for i in range(3):
                    for j in range(3):
                        subbox.append(board[3*x_qdrant+i][3*y_qdrant+j])
                seen = {}
                for char in subbox:
                    if char in seen:
                        return False
                    elif char != '.':
                        seen[char] = 1
        return True