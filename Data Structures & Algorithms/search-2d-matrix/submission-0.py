'''
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.

- so basically the matrix is sorted in ascending order

Return true if target exists within matrix or false otherwise.

example:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

well we need to look at the first and last elements of each sublist right?
if L < target < R then it has to be in that sublist
and we just do that for each sublist...hm that makes sense

what if we just performed binary search on each sublist lol

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def find_target_in_sublist(sublist, target):
            L, R = 0, len(sublist) - 1
            while L <= R:
                M = (R + L) // 2
                if sublist[M] < target:
                    L = M + 1
                elif sublist[M] > target:
                    R = M - 1
                else:
                    return True
            return False
        for i in range(len(matrix)):
            curr_list = matrix[i]
            if find_target_in_sublist(curr_list, target):
                return True
        return False