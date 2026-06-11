class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)

        
        for word in strs:
            letter_count = [0] * 26
            for c in word:
                letter_count[ord(c) - ord('a')] += 1
            grouped_anagrams[tuple(letter_count)].append(word)
        
        return list(grouped_anagrams.values())