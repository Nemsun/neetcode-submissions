class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
        for key, value in count_map.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            while freq[i]:
                res.append(freq[i].pop())
                if len(res) == k:
                    return res