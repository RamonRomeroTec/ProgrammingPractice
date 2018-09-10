#include <math.h>
#include <stdlib.h>
#include <stdio.h>

#include <math.h>

class Solution {
public:
    int reverse(int x) {
        long reverse=0;
        int sign=1;
       
        
        if (x == 0){
            return 0;
        }
        long int rev = (long)x;
        if(rev>2147483647||rev<-2147483647){
		    return 0;
	   }
        
        if (x<0){
            reverse=0;
            x=x*-1;
 	    int digits = (int)(log10(x)+1);
            for(int i=(digits-1); i>=0; i--){
                reverse += (long)(x%10)*(pow(10,i));
                x=x/10;
            }  
            
           reverse*=-1;
	   if(reverse>2147483647||reverse<-2147483647){
		return 0;
	   }
           return (int)reverse;
        }
        
        else{
	    int digits = (int)(log10(x)+1);     
            
            for(int i=(digits-1); i>=0; i--){
                reverse += (long)(x%10)*(pow(10,i));
                x=x/10;
            }
         
	    if(reverse>2147483647||reverse<-2147483647){
		return 0;
	    }   
            return (int)reverse;
        }
    }
};
int main(){
	Solution sol;
	printf("%d",sol.reverse(-99999));
}
