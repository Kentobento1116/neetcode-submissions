class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])

        if s1_count == s2_count:
            return True
        
        p1 = 0
        for p2 in range(len(s1), len(s2)):
            s2_count[s2[p2]] += 1
            s2_count[s2[p1]] -= 1

            p1 += 1

            if s1_count == s2_count:
                return True
        
        return False
            