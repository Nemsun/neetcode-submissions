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
        if len(nums) == 0:
            return 0
        longest = 1
        for i in range(len(nums)):
            if (nums[i] - 1) in nums:
                continue
            if (nums[i] + 1) in nums:
                curr_num = nums[i]
                cnt = 0
                while curr_num in nums:
                    cnt += 1
                    curr_num += 1
                longest = max(longest, cnt)
        return longest


                

