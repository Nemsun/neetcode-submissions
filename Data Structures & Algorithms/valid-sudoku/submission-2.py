class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = board[i]
            check_row = {}
            for j in range(len(row)):
                if row[j] == ".":
                    continue
                if row[j] in check_row:
                    return False
                else:
                    check_row[row[j]] = 1

        for j in range(len(board)):
            check_col = {}
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in check_col:
                    return False
                else:
                    check_col[board[i][j]] = 1

        for row in range(3):
            for col in range(3):
                check_square = {}
                for i in range(3):
                    for j in range(3):
                        if board[row * 3 + i][col * 3 + j] == ".":
                            continue
                        if board[row * 3 + i][col * 3 + j] in check_square:
                            return False
                        else:
                            check_square[board[row * 3 + i][col * 3 + j]] = 1
        return True