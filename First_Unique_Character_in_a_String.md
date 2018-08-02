# Description
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
```
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```
# Solution
Use a 26-bits array to store every letter in s, and if get the letter again, record it as -1. Last, we find the minimum positive number in the array and return -1 if we can't find a positive number.
# C++(24ms)
```cpp
class Solution {
public:
    int firstUniqChar(string s) {
        int count[26] = {0};
        int tem = 0;
        for(int i = 0;i < s.size();i ++)
        {
            tem = s[i] - 'a';
            if(count[tem]==0)
                count[tem] = i+1;
            else 
                if(count[tem]>0)
                    count[tem] = -1;
        }
        int flag = 1;
        int min = 1200000;
        for(int i=0;i<26;i++)
            if(count[i]>0)
            {min = count[i]<min?count[i]:min;flag = 0;}
        if(flag)
            return -1;
        return min-1;
    }
};
```
