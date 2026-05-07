class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupHash = set()

        for num in nums:
            if num in dupHash:
                return True
            dupHash.add(num)

        return False