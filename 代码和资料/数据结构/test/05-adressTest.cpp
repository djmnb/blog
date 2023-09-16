#include<iostream>
#include<windows.h>
using namespace std;
static int a = 10;
int main(){
    while(1){
        cout << &a << endl;
        cout << a << endl;
        Sleep(2000);
    }
}