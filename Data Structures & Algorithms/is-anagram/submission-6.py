class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1, arr2 = [], []
        

        # Add char
        for char in s:
            arr1.append(char)
        for char in t:
            arr2.append(char)

        arr1.sort()
        arr2.sort()
        # compare
        if arr1 == arr2: return True


        return False 