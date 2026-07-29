class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        for char in s:
            s_count[char] = 1 + s_count.get(char, 0)
        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)
        return s_count == t_count