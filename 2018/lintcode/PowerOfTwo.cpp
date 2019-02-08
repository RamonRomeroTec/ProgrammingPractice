// @AleLopez1312
// @ramonromerotec
//ok

class Solution {
public:
    /**
     * @param n: an integer
     * @return: if n is a power of two
     */
    bool isPowerOfTwo(int n) {
        // Write your code here
        if (n%2==0){
            isPowerOfTwo(n/2);
        }else if(n==1){
                        return true;


        }else {
            return false;
        }
    }
};
