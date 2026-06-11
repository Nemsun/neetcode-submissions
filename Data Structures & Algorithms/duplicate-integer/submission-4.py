class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_map = defaultdict(int)

        for num in nums:
            dupe_map[num] += 1
        
        for v in dupe_map.values():
            if v > 1:
                return True
        return False