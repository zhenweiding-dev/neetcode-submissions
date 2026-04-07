class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        i 9*9 board
        o T/F
        c 9*9, board[i][j]= "k", k = 1-9/.
        e 
        """
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                mask = 1 << (int(board[r][c]) - 1)

                if mask & rows[r]:
                    return False
                if mask & cols[c]:
                    return False
                if mask & squares[(r // 3) * 3 + (c // 3)]:
                    return False
                
                rows[r] |= mask
                cols[c] |= mask
                squares[(r // 3) * 3 + (c // 3)] |= mask
        return True
            

        