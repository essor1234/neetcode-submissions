class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length != t.length) return false;

        let firstDict = {};
        let secondDict = {};
        // Loop for s
        for(let word of s){
            if(word in firstDict){
                firstDict[word] += 1;
            }else{
                firstDict[word] = 1;
            }
             
        }
        // Loop for t
        for(let word of t){
            if(word in secondDict){
                secondDict[word] += 1;
            }else{
                secondDict[word] = 1;
            }
             
        }

        for(let word in firstDict){
            // If word in firstDict not exist in secondDict
            if(secondDict[word] == undefined){
                return false
            }
            // If the amount of word is not equal
            if(firstDict[word] != secondDict[word]){
                return false
            }

        }

        return true

    }
}
