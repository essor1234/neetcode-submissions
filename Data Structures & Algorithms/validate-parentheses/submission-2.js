class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const brackets = {
            "]": "[",
            "}" : "{",
            ")" : "("

        }
        const order = []
        
        for (let c of s){
            if (brackets[c]){
                if(order.length > 0 && brackets[c] === order[order.length-1]){
                    order.pop()
                }else{
                    return false
                }
            }else{
                order.push(c)
                
            }
        }
        return order.length == 0

    }
}
