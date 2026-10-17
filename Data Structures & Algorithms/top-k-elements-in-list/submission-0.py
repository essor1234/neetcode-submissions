class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result =[]

        # create and update hashmap
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        # Get result
        sorted_items = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        for items in sorted_items:
            if k >0:
                result.append(items[0])
                k-=1
        return result
        

