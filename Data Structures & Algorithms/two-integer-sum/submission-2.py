class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            curr_diff = target - nums[i]
            if curr_diff in seen:
                return [seen[curr_diff], i]
            seen[nums[i]] = i
        return []