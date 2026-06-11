'''
You are given an array of length n which was originally sorted in ascending order. 
It has now been rotated between 1 and n times. 

- values are sorted already in ascending order
- so no matter what the left < right

For example, the array nums = [1,2,3,4,5,6] might become:
- [3,4,5,6,1,2] if it was rotated 4 times.
- [1,2,3,4,5,6] if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning. 
Rotating the array 6 times produces the original array.

- so rotating just means shifting to the right by one

Assuming all elements in the rotated sorted array nums are unique, 
return the minimum element of this array.

- no duplicate numbers

A solution that runs in O(n) time is trivial, 
can you write an algorithm that runs in O(log n) time?

- binary search or something

example:
nums = [3,4,5,6,1,2]
output = 1

what if start from the middle then go from there? since we know that a sorted list
if middle value < right value -> then we know that the min is in the left

'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        min_val = float("inf")

        while (L < R):
            M = (L + R) // 2
            min_val = min(min_val, nums[M])

            if nums[M] < nums[R]:
                R = M - 1
            else:
                L = M + 1
        
        return min(min_val, nums[L])
        