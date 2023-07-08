#include <iostream>
#include <vector>
#include <string>
using namespace std;

void getNext(string &str, vector<int> &next)
{

    int i = 0, j = -1;
    int len = str.length();

    // 第0个字符都匹配失败的话, 就是退到-1了
    next.push_back(-1);

    // 由于next[i+1] 的值是由前i个字符决定的, 因此, 我们只需要将i计算到  len-2
    while (i < len - 1)
    {
        // next[i+1] 的值是由前i个字符决定的, j==-1其实也是一种 str[i] == str[j] 只不过str[-1] 是一种不存在的存在
        if (j == -1 || str[i] == str[j])
        {
            // 由于str[i] == str[j]  所以 next[i+1] = j+1  也就是 如果当前元素匹配失败, 应该要回退到j+1这个位置继续匹配
            ++i;
            ++j;

            if (str[i] == str[j])
            {
                next.push_back(next[j]);
            }
            else
            {
                next.push_back(j);
            }
        }
        else
        {
            // 如果str[i] != str[j]  就要去找next[j] 看他们是否相等
            j = next[j];
        }
    }
}

int funcKMP(string mainstr, string substr)
{

    vector<int> next;
    getNext(substr, next);

    int i = 0, j = 0; // 这里的j只需要从0 开始, 它是代表子串的位置, 而不是回退的位置, 在求next算法中 j是代表回退的位置
    int len = mainstr.length();
    int len1 = substr.length();
    while (i < len)
    {
        if (j == -1 || mainstr[i] == substr[j])
        {
            ++i;
            ++j;
        }
        else
        {
            j = next[j];
        }

        if (j == len1)
        {
            return i - j;
        }
    }
    return -1;
}

int main()
{
    string mainstr = "abaabcaba";
    string substr = "a";

    cout << funcKMP(mainstr, substr) << endl;
}