# Description
Given an integer, write a function to determine if it is a power of three.

Example 1:
```
Input: 27
Output: true
```
Example 2:
```
Input: 0
Output: false
```
Example 3:
```
Input: 9
Output: true
```
# Solution
Because this function is to determine if the number is a power of three. So, we can let the number to divide 3 continuously and if the remainder is not zero, return false. If the last number is one, return true.
# C++(52ms)
```cpp
class Solution {
public:
    bool isPowerOfThree(int n) {
        while(!(n%3) && n>1)
            n /= 3;
        if(n==1)
            return true;
        return false;
    }
};
```
