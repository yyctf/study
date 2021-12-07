#include <stdio.h>
int backdoor(){

    system("/bin/sh");
}

int main(){
    backdoor();
}
