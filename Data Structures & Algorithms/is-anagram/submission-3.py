class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        saved = {} # word : amount

        pointer = 0
        # put word from s into dict
        for i, w in enumerate(s):
            print(f"i {i}, w: {w}")
            # Update if already in the dict
            if w in saved:
                saved[w] += 1
            else:
                saved[w] = 1

        print(saved)
        # Check if enough char in the t compare to dict
        for i, w in enumerate(t):
            if w in saved and saved[w] >=0:
                print(saved[w])
                saved[w] -= 1
            else:
                return False

        for val in saved.values():
            if val != 0:
                return False
        return True
        