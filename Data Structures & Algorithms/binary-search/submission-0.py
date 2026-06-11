'''
You are given an array of distinct integers nums, 
sorted in ascending order, and an integer target.

- ascending order, target int
- find the integer
- loop through list of numbers

Implement a function to search for target within nums. 

If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.
- so must divide list in half each way
- find the middle of the list

potentional solution:
- two ptr solution
- mid = R - L // 2
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + ((R - L) // 2)
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                return mid
        return -1
        