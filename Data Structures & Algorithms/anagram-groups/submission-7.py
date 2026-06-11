class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            char_arr = [0] * 26
            for c in word:
                char_arr[ord(c) - ord('a')] += 1
            anagrams[tuple(char_arr)].append(word)
        return list(anagrams.values())