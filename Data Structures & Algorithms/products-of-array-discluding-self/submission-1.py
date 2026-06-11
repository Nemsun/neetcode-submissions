class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiples = []
        curr_product = 1
        for i in range(len(nums)):
            multiples.append(curr_product)
            curr_product *= nums[i]

        curr_product = 1
        for i in range(len(nums) - 1, -1, -1):
            multiples[i] *= curr_product
            curr_product *= nums[i]
            
        return multiples

        
            
