
/*
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){

    long long int i,num,k,x,y;
    while(scanf("%lli", &k) != EOF){
        num=0;
        for(i=k+1; i<=2*k; i++){
            if((i*k)%(i-k)==0)
                num++;
        }
        printf("%lli\n", num);

        for(i=k+1; i<=2*k; i++){
            if((i*k)%(i-k)==0){
                x=(i*k)/(i-k);
                y=i;
                printf("1/%lli = 1/%lli + 1/%lli\n", k, x, y);
            }
        }
    }
    return 0;
}
*/