class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for i in nums:
            result.add(i)
        return len(nums) != len(result)