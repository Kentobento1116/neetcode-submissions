class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        p1 = 0
        max_len = 0

        for p2 in range(len(s)):
            while s[p2] in char_set:
                char_set.remove(s[p1])
                p1 += 1

            char_set.add(s[p2])
            max_len = max(max_len, p2 - p1 + 1)
        return max_len
        