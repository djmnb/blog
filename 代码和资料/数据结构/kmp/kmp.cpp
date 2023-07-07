#include <iostream>
#include <vector>
#include <string>
using namespace std;

void getNext(string &str, vector<int> &next)
{

    int i = 0, j = -1;
    next.clear();

    int len = str.length();
    cout << len << endl;
    next.assign(len, -1);

    next[0] = -1;

    while (i < len-1)
    {
        if (j == -1 || str[i] == str[j])
        {
            ++i;
            ++j;
            next[i] = j;
        }
        else
        {
            j = next[j];
        }
    }
}

int main()
{
    string str = "abaabcaba";
    vector<int> next;
    getNext(str, next);

    for (int i : next)
    {
        cout << i << " ";
    }
}