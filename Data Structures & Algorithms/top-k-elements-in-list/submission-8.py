class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        bins = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count_map[num] += 1
        
        for num, cnt in count_map.items():
            bins[cnt].append(num)
        
        res = []
        for i in range(len(bins) - 1, 0, -1):
            for num in bins[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res