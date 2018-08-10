# Description
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:
```
Input: 6
Output: true
Explanation: 6 = 2 × 3
```
Example 2:
```
Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
```
Example 3:
```
Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
```
# Solution
The loop also is a useful way to solve easy problems.
# C++(4ms)
```cpp
class Solution {
public:
    bool isUgly(int num) {
        if(num <= 0)
            return false;
        while( !(num%2) || !(num%3) || !(num%5))
        {
            if(num%2 == 0)
                num /= 2;
            else if(num % 3 == 0)
                num /= 3;
            else
                num /= 5;
        }
        if(num == 1)
            return true;
        return false;
    }
};
```
