class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"]": "[", ")":"(", "}":"{"}
        saved = []

        for c in s:
            # if open bracket
            if c in brackets.values():
                saved.append(c)
            # if close bracket
            elif c in brackets:
                if not saved or saved[-1] != brackets[c]:
                    return False
                else:
                    saved.pop()

        return len(saved) == 0

            

