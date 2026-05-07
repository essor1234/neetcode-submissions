class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Need 2 pointers, one at the start,  one at the end
        # Loop through the string until two pointers meet
        # Loop to get through symbol that not in isalnum() [both side]
        # check if the char is the same 
        # update value
        
        start, end = 0, len(s)-1

        while start < end:
            # Passing through char that not in alphabet or numerate
            while start < end and not s[start].isalnum():
                start +=1

            while start < end and not s[end].isalnum():
                end -= 1 
            # Check if they are the same
            if s[start].lower() != s[end].lower():
                return False

            # update the start and end position
            start += 1
            end -=1

        return True

            
            

            
        