#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

int vul(){

    char buffer[64];
    puts("puts");
    gets(buffer);
}
int main(){

    vul();
    return 0;
}
