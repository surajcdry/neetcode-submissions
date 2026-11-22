class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCount = {}

        for n in nums:
            if n in numCount:
                return True
            else:
                numCount[n] = 1
        return False