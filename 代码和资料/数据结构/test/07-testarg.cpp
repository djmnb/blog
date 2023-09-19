#include <iostream>
using namespace std;

int add(int a, int b)
{

    int *c = &b;
    int *d = c - 2;
    cout << *d << endl;
    cout << *c << endl;

    cout << &a << " " << &b << endl;

    return a + b;
}

int main()
{
    int a = 10, b = 20;
    add(a, b);
}