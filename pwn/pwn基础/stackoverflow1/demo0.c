#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int vulnerable_function(){
    char buffer[32];
    printf("please input something: \n");
    gets(buffer);
    return 0;
}

int backdoor(){
    system("/bin/sh\x00");
    return 0;
}

int main(){

    printf("hello,world! \n");
    vulnerable_function();
    printf("bye~!\n");
    return 0;
}
