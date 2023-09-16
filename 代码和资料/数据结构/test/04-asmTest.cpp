
#include <iostream>
using namespace std;
int add(int x, int y)
{
    return x + y;
}

int caller()
{
    int a = 10, b = 10;
    int sum = add(a, b);
    return sum;
}

int main()
{
    cout << __FILE__ << endl;
    cout << __LINE__ << endl;
}
