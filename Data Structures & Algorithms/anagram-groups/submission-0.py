class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap moment lol
        # key: list of counts of the characters, value: word list

        anagrams = defaultdict(list)

        for _str in strs:
            count = [0] * 26
            for c in _str:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(_str)

        return anagrams.values()
