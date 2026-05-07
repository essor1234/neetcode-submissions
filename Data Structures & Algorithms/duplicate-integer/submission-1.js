class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hashMap = new Set();

        for (let i=0; i<nums.length;i++){
            console.log(nums[i] in hashMap);
            if (hashMap.has(nums[i])){
                return true
            }else{
                hashMap.add(nums[i])
            }
        }
        console.log(hashMap)
        return false
    }
}

