class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posdiag = set()
        negdiag = set()
        res = []
        board = [["."]*n for i in range(n)]
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)

            for c in range(n):
                if c in cols or (c+r) in posdiag or c-r in negdiag:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                posdiag.add(c+r)
                negdiag.add(c-r)

                dfs(r+1)
                board[r][c] = "."
                cols.remove(c)
                posdiag.remove(c+r)
                negdiag.remove(c-r)
        dfs(0)
        return res