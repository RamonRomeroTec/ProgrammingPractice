#include <stdio.h>

int main() {
    int cases;
    scanf("%i", &cases);
    char str [5];
    int suma=0;
    for (int i = 0; i < cases; i++) {
        scanf("%s", str);
        if(str[1]=='+'){
            suma++;
        } else{
            suma--;
        }



    }

    printf("%i", suma);
    return 0;
}
