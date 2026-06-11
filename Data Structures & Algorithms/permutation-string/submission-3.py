class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        A, B = s1, s2

        if len(A) > len(B):
            return False
        L = 0
        A = ''.join(sorted(A))
        for R in range(len(A), len(B) + 1):
            curr_substr = ''.join(sorted(B[L:R]))
            print(curr_substr)
            if A in curr_substr:
                return True
            L += 1
        return False