'''
Given a string s, find the length of the longest substring without duplicate characters.
- longest substring? -> sliding window
A substring is a contiguous sequence of characters within a string.

sliding window approach
- increase our window until we see a duplicate character within our substring
- if we see a char in str -> move pointer to the left, continouously move right pointer
Input: s = "zxyzxyz"

Output: 3


'''
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
            longest = max(longest, (R - L + 1))
        
        return longest