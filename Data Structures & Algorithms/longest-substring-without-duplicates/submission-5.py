class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_substr = set()
        longest = 0
        L = 0

        for R in range(len(s)):
            while s[R] in curr_substr:
                curr_substr.remove(s[L])
                L += 1
            curr_substr.add(s[R])
            longest = max(longest, R - L + 1)
        return longest