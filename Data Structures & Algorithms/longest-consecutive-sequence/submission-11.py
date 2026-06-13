class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        length = 0 
        for num in nums:
            if (num - 1) not in num_set:
                curr_length = 1
                while (curr_length + num) in num_set:
                    curr_length += 1
                length = max(length, curr_length)
        return length