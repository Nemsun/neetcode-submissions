class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        TOP, BOT = 0, ROWS - 1

        while TOP <= BOT:
            CURR_ROW = (TOP + BOT) // 2
            if matrix[CURR_ROW][-1] < target:
                TOP = CURR_ROW + 1
            elif matrix[CURR_ROW][0] > target:
                BOT = CURR_ROW - 1
            else:
                break
        
        if not (TOP <= BOT):
            return False
        CURR_ROW = (TOP + BOT) // 2
        L, R = 0, COLS - 1
        while L <= R:
            M = (L + R) // 2
            if matrix[CURR_ROW][M] < target:
                L = M + 1
            elif matrix[CURR_ROW][M] > target:
                R = M - 1
            else:
                return True
        return False