class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {

        const hashMap = {};

        for(let i=0; i<nums.length;i++){
            let cal = target - nums[i]
            // console.log(nums.indexOf)
            if(cal in hashMap){
                return [hashMap[cal], i]
            }
            hashMap[nums[i]] = i

        }
        return []
    }
}
