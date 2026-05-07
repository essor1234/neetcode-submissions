class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let left = 0
        let right = nums.length -1

        while(left<=right){
            let mean = Math.floor((left+right)/2)
            if(nums[mean] === target) return mean;
            if(nums[mean] < target){
                left = mean+1
            }else{
                right = mean-1
            }

        }
        return -1
    }
}
