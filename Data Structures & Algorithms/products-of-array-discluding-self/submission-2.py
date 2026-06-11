class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        
        prefix[0] = suffix[-1] = 1

        # prefix contains all previous elements multiplied by each other except the current
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        # suffix contains all after elements multipled by each other except the current
        for i in range(n - 2, -1 ,-1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        res = [0] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res