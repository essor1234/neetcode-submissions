class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        result = []
        # key: []

        for word in strs:
            key_word = "".join(sorted(word))
            if key_word in hashmap:
                hashmap[key_word].append(word)
            else:
                hashmap.setdefault(key_word, []).append(word)

        # Get the result
        for key, value in hashmap.items():
            result.append(value)
        return result
        