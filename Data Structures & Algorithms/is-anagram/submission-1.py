class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount = collections.Counter(s)

        for c in t:
            if sCount[c] == 0:
                return False
            sCount[c] -= 1
        
        return True