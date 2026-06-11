class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hashset to record the difference
        # if the current number had equal the difference we found our match
        diff_table = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in diff_table:
                return [diff_table[nums[i]], i]
            diff_table[diff] = i
        return []