class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            row = top + (bot - top) // 2
            if matrix[row][0] <= target:
                top = row + 1
            elif matrix[row][-1] > target:
                bot = row - 1
            else:
                break

        row = top + (bot - top) // 2
        lo, up = 0, len(matrix[0]) - 1
        while lo <= up:
            mid = lo + (up - lo) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                up = mid - 1
        return False