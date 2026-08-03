class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        max_left, max_right = height[L], height[R]
        water = 0
        while L < R:
            if max_left < max_right:
                L += 1
                max_left = max(max_left, height[L])
                water += max_left - height[L]
            else:
                R -= 1
                max_right = max(max_right, height[R])
                water += max_right - height[R]
        return water