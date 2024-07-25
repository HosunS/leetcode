class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        '''
        keep a counter of how many pawns can be attacked
        when we iterate through the matrix from the Rook, we need to increment the row and columns
        in seperate directions to figure out whether there is a pawn or not.
        left = [col - 1]  , right = [col + 1], up = [row -1], down = [row + 1]

        iterate until we reach Rook, and iterate each direction until we hit 7
        '''

        pawnsAttacked = 0
        row = 0
        col = 0
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    row = r
                    col = c
                    
        rook = (row , col)
        i = 0

        for i in range(row -1, -1 , -1):
            if board[i][col] == 'p':
                pawnsAttacked += 1
                break
            elif board[i][col] == 'B':
                break

        for i in range(col -1, -1 , -1):
            if board[row][i] == 'p':
                pawnsAttacked += 1
                break
            elif board[row][i] == 'B':
                break

        for i in range(row + 1, 8):
            if board[i][col] == 'p':
                pawnsAttacked += 1
                break
            elif board[i][col] == 'B':
                break

        for i in range(col + 1 , 8):
            if board[row][i] == 'p':
                pawnsAttacked += 1
                break
            elif board[row][i] == 'B':
                break
        return pawnsAttacked
