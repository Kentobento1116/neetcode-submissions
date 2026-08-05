class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in range(len(s)):
            if s[i] in ('(', '{', '['):
                stack.append(s[i])
            if s[i] in (')', '}', ']'):
                if not stack or stack.pop() != bracket_map[s[i]]:
                    return False
        return len(stack) == 0