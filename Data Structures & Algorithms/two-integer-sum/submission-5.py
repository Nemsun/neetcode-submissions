class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i, e in enumerate(nums):
            curr_diff = target - e
            if curr_diff in diffs:
                return [diffs[curr_diff], i]
            diffs[e] = i
        return []