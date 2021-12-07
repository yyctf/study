#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

char buf[64];

int vul(){

    char buffer[64];
    printf("please input something: \n");
    gets(buffer);
    strncpy(buf,buffer,64);
    printf("bye~!\n");
    return 0;
}
int main(){

    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,1,0);

    vul();
    return 0;
}
