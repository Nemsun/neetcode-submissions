'''
You are given an array of length n which was originally sorted in 
ascending order. It has now been rotated between 1 and n times. 

For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.

Given the rotated sorted array nums and an integer target,
return the index of target within nums, or -1 if it is not present.

- perform normal binary search
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            M = L + (R - L) // 2
            
            if nums[M] == target:
                return M

            if nums[L] <= nums[M]:
                if target > nums[M] or target < nums[L]:
                    L = M + 1
                else:
                    R = M - 1
            else:
                if target < nums[M] or target > nums[R]:
                    R = M - 1
                else:
                    L = M + 1
        return -1
        