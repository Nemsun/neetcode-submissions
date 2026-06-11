class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            L, R = i + 1, len(nums) - 1

            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            while (L < R):
                if (nums[L] + nums[R] + nums[i] > 0):
                    R -= 1
                elif (nums[L] + nums[R] + nums[i] < 0):
                    L += 1
                elif (nums[L] + nums[R] + nums[i] == 0):
                    triplets.append([nums[i], nums[L], nums[R]])
                    
                    L += 1

                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        return triplets
