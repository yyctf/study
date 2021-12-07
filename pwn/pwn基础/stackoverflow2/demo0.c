#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

char buf[] = "sh";
int vulnerable_function(){
    char buffer[32];
    printf("please input something: \n");
    gets(buffer);
    return 0;
}

int sys(){
    system("ls");
}

int main(){

    printf("hello,world! \n");
    vulnerable_function();
    printf("bye~!\n");
    return 0;
}
