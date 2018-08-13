# Description
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# Solution
Emmmm, it's a old problem, but I think I do this better than I did before.
# C++(8ms)
```cpp
class Solution {
public:
    string addStrings(string num1, string num2) {
        int len1 = num1.size();
        int len2 = num2.size();
        string re = "";
        int i, j, flag = 0, tem = 0;
        for(i = len1 - 1,j = len2 - 1;i >=0 && j >= 0;i--,j--)
        {
            tem = (num1[i] - '0') + (num2[j] - '0') + flag;
            flag = tem / 10;
            re = to_string(tem%10) + re;
        }
        for(;i>=0;i --)
        {
            tem = num1[i] - '0' + flag;
            flag = tem/10;
            re = to_string(tem%10) + re;
        }
        for(;j>=0;j --)
        {
            tem = num2[j] - '0' + flag;
            flag = tem/10;
            re = to_string(tem%10) + re;
        }
        if(flag)
            re = to_string(flag) + re;
        return re;
    }
};
```
