class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = collections.Counter(s)

        for c in t:
            if c not in sCount or sCount[c] - 1 < 0:
                return False
            sCount[c] -= 1
        
        return True if max(sCount.values()) == 0 else False