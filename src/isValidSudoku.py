from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isDuplicate(row):
                return False
            
        for col in zip(*board):
            if not self.isDuplicate(col):
                return False
            
        # Check 3x3 subgrids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.isDuplicate([board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]):
                    return False
        
        return True

    def isDuplicate(self, array_to_search):
        seen = set()
        for square in array_to_search:
            if square != '.':
                if square in seen:
                    return False
                seen.add(square)
        return True



c = Solution()
print(c.isValidSudoku(board = 
[[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
))