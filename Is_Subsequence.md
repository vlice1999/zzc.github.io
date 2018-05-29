## 题目描述
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

## 解题思路
特意挑了一个简单的题哈哈哈，没什么好解释的，直接for就ＯＫ了

## C++(71ms)
```cpp
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int l1=s.size();
        int l2=t.size();
        if(l1==0)
            return true;
        if(l2==0)
            return false;
        for(int i=0,j=0;i<l2;i++)
        {
            if(s[j]==t[i])
                j++;
            if(j==l1)
                return true;
        }
        return false;
    }
};
```
