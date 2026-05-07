class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        # Add chars of s into the hashmap, count up 
        for c in s:
            if c not in hashmap:
                hashmap[c] = 0
            hashmap[c] +=1
        for c in t:
            if c not in hashmap:
                return False

            hashmap[c] -= 1

        #Check final result
        # case 1: if all counting already 0
        for v in hashmap.keys():
            print(hashmap[v])
            if hashmap[v] != 0:
                return False

        return True