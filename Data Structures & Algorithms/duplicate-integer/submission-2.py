class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Having a dictionay
        # loop through the list
        # add value into dict
        # if duplicate, return True

        check = {}
        for num in nums:
            if num in check.keys():
                return True
            else:
                check[num] = 0
        return False