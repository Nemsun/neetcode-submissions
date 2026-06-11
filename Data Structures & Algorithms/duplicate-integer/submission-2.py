class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = {}

        for i in nums:
            num_map[i] = num_map.get(i, 0) + 1
            if num_map[i] > 1:
                return True
        return False