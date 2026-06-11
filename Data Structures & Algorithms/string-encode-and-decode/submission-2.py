class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        output = strs[0]
        for i in range(1, len(strs)):
            output = output + ";" + strs[i]
        return output + ";"
    
    def decode(self, s: str) -> List[str]:
        words = []
        curr_word = ""
        for i in range(len(s)):
            curr_word += s[i]
            if s[i] == ";":
                words.append(curr_word[:-1])
                curr_word = ""
        return words