class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # base case
        # if len(nums) == 0:
        #     return 0
        # sorting + removing dupes
        # sorted_nums = sorted(list(set(nums)))

        # cnt = 1
        # longest = 1
        # for i in range(1, len(sorted_nums)):
        #     if (sorted_nums[i-1] + 1) == sorted_nums[i]:
        #         cnt += 1
        #     else:
        #         longest = max(longest, cnt)
        #         cnt = 1
        
        # longest = max(longest, cnt)
        
        # return longest
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


                

