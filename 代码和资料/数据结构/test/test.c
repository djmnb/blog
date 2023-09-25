#include <stdio.h>
void my_entry()
{
    // your code here
    while (1)
    {
        printf("my_entry");
        getchar();
    }
}

int main()
{
    // This will not be called
    printf("main");

    getchar();
    return 0;
}

__attribute__((section(".init"))) void another_entry()
{
    asm("call my_entry");
}
