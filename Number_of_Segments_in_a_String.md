# Description
Pick One

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.
Example:
```
Input: "Hello, my name is John"
Output: 5
```
# Solution
First, I set a flag to judge if I get a new word. If the letter is space, flag is true. Otherwise, flag is false. And if the flag is true and the letter is not space, I get a new word.
# C++(0ms)
```cpp
class Solution {
public:
    int countSegments(string s) {
        int re = 0;
        bool flag = 1;
        for(int i = 0;i < s.size();i ++){
            if(flag && s[i] != ' ')
                re ++;
            if(s[i]==' ')
                flag = 1;
            else
                flag = 0;
        }
        return re;
    }
};
```
