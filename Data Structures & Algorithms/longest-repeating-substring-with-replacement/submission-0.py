class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        L = 0
        most_freq = 0
        for R in range(len(s)):
            char_freq[s[R]] = 1 + char_freq.get(s[R], 0)
            most_freq = max(char_freq[s[R]], most_freq)

            if (R - L + 1) - most_freq > k:
                char_freq[s[L]] -= 1
                L += 1
        return (R - L + 1)