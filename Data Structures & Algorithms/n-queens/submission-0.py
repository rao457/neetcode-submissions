class Solution:
    def isSafe(self, board, row, col, n):
        # horizontal
        for i in range(n):
            if board[row][i] == "Q":
                return False
        
        # Vertical

        for j in range(n):
            if board[j][col] == "Q":
                return False
        
        # Left Diagonal
        i = row
        j = col
        while (i >= 0 and j >= 0):
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        
        # Right Diagonal 
        a = row
        b = col
        while (a >= 0 and b < n):
            if board[a][b] == "Q":
                return False
            a -= 1
            b += 1
        return True

    def nQueens(self, board, row, n, ans):
        if (row == n):
            ans.append(["".join(r) for r in board])
            return
        for j in range(n):
            if self.isSafe(board, row, j, n):
                board[row][j] = "Q"
                self.nQueens(board, row+1, n, ans)
                board[row][j] = "."
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        ans = []
        self.nQueens(board, 0, n, ans)
        return ans