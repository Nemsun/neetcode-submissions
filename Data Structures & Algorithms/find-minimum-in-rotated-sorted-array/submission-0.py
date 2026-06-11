class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = float('inf')
        for n in nums:
            if n < min_num:
                min_num = n
        
        return min_num

