class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hasArr = set()
        for num in nums:
            if num in hasArr:
                return True

            hasArr.add(num)

        return False