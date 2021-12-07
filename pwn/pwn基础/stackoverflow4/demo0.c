#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

char* sh = "/bin/sh";
int vul(){

    char buffer[64];
    printf("please input something: \n");
    gets(buffer);
}
int main(){

    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,1,0);

    vul();
    return 0;
}
