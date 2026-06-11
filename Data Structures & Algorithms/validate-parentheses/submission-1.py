class Solution:
    def isValid(self, s: str) -> bool:
        brack_map = {')': '(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c not in brack_map:
                stack.append(c)
                continue
            if not stack or stack[-1] != brack_map[c]:
                return False
            stack.pop()
        return not stack
