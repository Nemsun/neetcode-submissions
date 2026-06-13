class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prod *= prefix[i] * nums[i - 1]
            prefix[i] = prod
        prod = 1
        suffix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            prod *= suffix[i] * nums[i + 1]
            suffix[i] = prod
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = prefix[i] * suffix[i]
        return ans