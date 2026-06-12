class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bins = [[] for _ in range(len(nums) + 1)]
        res = []
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        for val, freq in freq_map.items():
            bins[freq].append(val)
        for i in range(len(bins) - 1, -1, -1):
            while bins[i]:
                res.append(bins[i].pop())
                if len(res) == k:
                    return res
        return res