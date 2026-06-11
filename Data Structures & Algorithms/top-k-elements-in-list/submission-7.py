class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq_bin = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1

        for num, cnt in count.items():
            freq_bin[cnt].append(num)

        res = []
        for i in range(len(freq_bin) - 1, 0, -1):
            for num in freq_bin[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res