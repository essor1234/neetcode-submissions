class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Check the length of them
        # Need a pointer
        # Need a dictionary
        # Add and calculate the number of words based on first string
        # Recalculate the number of words based on second string
        # Check if the remain of the calculate

        #+===============#===================#
        # Checking the lenght of both string
        if len(s) != len(t): return False

        p = 0 # Pointer start from 0
        saved = {} # word:count
        
        # Getting through the first string
        for i, w in enumerate(s):
            # if already exist -> increase count
            # else -> add new (default 1)
            if w in saved:
                saved[w] += 1
            else:
                saved[w] = 1

        # Getting through the second string
        for i , w in enumerate(t):
            # if word in dict -> decrease count
            # else -> return False
            if w in saved:
                saved[w] -= 1
            else:
                return False

        # Getting through the dictionary
        for count in saved.values():
            # If any values != 0 -> return False
            if count != 0:
                return False

        return True


        

        