class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        const store = {}
        for(let i=0;i<numbers.length;i++){
            let cal = target - numbers[i]
            if(cal in store){
                return [store[cal], i+1]
            }
            store[numbers[i]] = i+1
            
        }
        return []
    }
}
