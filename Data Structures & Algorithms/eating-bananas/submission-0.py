class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        ans = R

        while L <= R:
            k = (L + R) // 2

            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / k)
            
            if total_time <= h:
                ans = k
                R = k - 1
            else:
                L = k + 1
        
        return ans
