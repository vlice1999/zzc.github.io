# Description
Given an integer, return its base 7 string representation.

Example 1:
```
Input: 100
Output: "202"
```
Example 2:
```
Input: -7
Output: "-10"
```
# Solution
I think the loop is also a good way to solve this problem. Emmm,,,
# C++(4ms)
```cpp
class Solution {
public:
    string convertToBase7(int num) {
        string re = "";
        int flag = 0;
        if(num < 0)
            flag = 1;
        num = abs(num);
        if(num == 0)
            re = to_string(0);
        while(num){
            re = to_string(num%7) + re;
            num/= 7;
        } 
        if(flag)
            re = '-' + re;
        return re;
    }
};
```
