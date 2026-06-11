class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            characters[ord(s[i]) - ord('a')] += 1
            characters[ord(t[i]) - ord('a')] -= 1
        
        for val in characters:
            if val != 0:
                return False
        return True  