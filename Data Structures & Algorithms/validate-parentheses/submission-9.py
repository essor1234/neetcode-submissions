class Solution:


    # Need a dict that contain {"close bracket": "open bracket"}
    # Need a list to checkout the order of the bracket
    # Need to get through all the char
    # Check for open bracket and close bracket
    ## Add new open bracket into the checking list
    ## Check if the list is empty of the last char in the list 
    ## is equal with the closest close bracket 
    ## Return False if not, or pop the last if yes
    ## Check the final lenght of the list if == 0
    def isValid(self, s: str) -> bool:
        brackets = {"]": "[", ")":"(", "}":"{"}
        saved = []

        for c in s:
            if c in brackets.values():
                saved.append(c)

            if c in brackets:
                if saved and saved[-1] == brackets[c]:
                    saved.pop()
                else: return False 


        return len(saved) == 0


