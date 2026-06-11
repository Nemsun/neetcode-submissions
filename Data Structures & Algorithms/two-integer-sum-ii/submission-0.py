class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        L, R = 0, len(numbers) - 1

        for i in range(len(numbers)):
            num_sum = numbers[L] + numbers[R]
            if num_sum == target:
                return [L + 1, R + 1]
            if num_sum > target:
                R -= 1
            elif num_sum < target:
                L += 1
        return []
