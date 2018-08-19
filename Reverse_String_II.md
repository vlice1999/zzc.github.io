# Description
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
```
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
```
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
# Solution
I used two ways to solve this problem. The first way is using `C++ reverse` function and the second way is using loop to relize reverse-function.
# C++
```cpp
// FIRST WAY: using `C++ reverse` function
// TIME: 4ms
class Solution {
public:
    string reverseStr(string s, int k) {
        string re = "";
        string tem = "";
        int count = 0, i = 0;
        if(k == 0)
            return s;
        
        for(;i < s.size(); i += k)
        {
            tem = s.substr(i, k);
            if(count % 2 == 0)
                reverse(tem.begin(), tem.end());
            count ++;
            re = re + tem;
        }

        return re;
    }
};
```
```cpp
// SECOND WAY: using loop to relize reverse-function
// TIME: 8ms
class Solution {
public:
    string reverseStr(string s, int k) {
        string re = "";
        string tem = "";
        int count = 0, i = 0;
        
        if(k == 0)
            return s;
        
        for(;i < s.size(); i += k)
        {
            if(count % 2 == 0){
                if(i + k < s.size())
                    for(int j = i + k-1;j >= i;j --)
                        re += s[j];
                else
                    for(int j = s.size() - 1;j >= i;j --)
                        re += s[j];
            }
            
            else
                for(int j = i;j < i + k && j<s.size();j ++)
                    re += s[j];
            count ++;
        }

        return re;
    }
};
```
