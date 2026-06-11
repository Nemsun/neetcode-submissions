class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set
        # time complexity O(1)
        # space complexity O(n)

        dupe_set = set(nums)

        return len(dupe_set) != len(nums)