class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    alphaNum(c){
        return (
             c >="a" && c<="z" ||
             c >="A" && c <= "Z" ||
             c >="0" && c <="9"
        )
    }
    isPalindrome(s) {
    
        let pointer1 = 0 //left
        let pointer2 = s.length-1 //right
        
        while(pointer1 < pointer2){
            while(pointer1 < pointer2 &&  !this.alphaNum(s[pointer1])){
                pointer1++
            }

            while(pointer1 < pointer2 &&  !this.alphaNum(s[pointer2])){
                pointer2--
            }
            if(s[pointer1].toLowerCase() !== s[pointer2].toLowerCase()){
                return false
            }

            pointer1++
            pointer2--
        }
        return true
    }
}
