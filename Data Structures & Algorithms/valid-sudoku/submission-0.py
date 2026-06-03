class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        box = set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == '.':
                    continue
                row_key = (r, num)
                col_key = (c, num)
                box_key = (r//3, c//3, num)

                if row_key in rows or col_key in cols or box_key in box:
                    return False
                rows.add(row_key)
                cols.add(col_key)
                box.add(box_key)
        return True