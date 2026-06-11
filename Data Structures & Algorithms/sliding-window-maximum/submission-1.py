class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_stack = []

        L, R = 0, k
        n = len(nums)
        
        while R <= n:
            curr_max = nums[L]
            for i in range(L, R):
                if curr_max < nums[i]:
                    curr_max = nums[i]
            max_stack.append(curr_max)
            L += 1
            R += 1
        return max_stack
            
            
        