class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_table = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_table:
                return [diff_table[diff], i]
            diff_table[nums[i]] = i
        return []