class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphabet = set('abcdefghijklmnopqrstuvwxyz0123456789')
        L, R = 0, len(s) - 1
        while L < R:
            while L < R and s[L] not in alphabet:
                L += 1
            while R > L and s[R] not in alphabet:
                R -= 1
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True
            