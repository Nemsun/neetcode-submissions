class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        maxLeft[0] = height[0]
        maxRight[len(height) - 1] = height[len(height) - 1]

        
        for i in range(1, len(height)):
            maxLeft[i] = max(height[i], maxLeft[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(height[i], maxRight[i + 1])

        trapped = 0
        for i in range(len(height)):
            curr_water = min(maxRight[i], maxLeft[i]) - height[i]
            if curr_water < 0:
                trapped += 0
            else:
                trapped += curr_water
        return trapped



