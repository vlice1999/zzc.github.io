# Description
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
```
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
```
Example 2:
```
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
```
# Solution
This problem have four possibilities. 

Fristly, if 1 + 2 + ... + n is equal to target, return n. 
Secondly, if (1 + 2 +...+ n) substract target is even, return n. If we substract n, the sum will be substracted 2n(>=2). 
Thirdly, if the sum substract target is odd and n is even, return n+1. As the second possibility, the (n+1) is odd, so if we add a new number, the sum will be increased from -2n-1 to n+1. And if the n is odd, return n+2. Becuase (n+1) is even  and (n+2) is odd.
# C++(0ms)
```cpp
class Solution {
public:
    int reachNumber(int target) {
        int tem = 1;
        target = abs(target);
        while(tem*(tem + 1)/2 < target)
            tem ++;
        if((tem*(tem + 1)/2 - target)%2 == 0)
            return tem;
        if(tem % 2 == 0)
            return tem + 1;
        return tem + 2;
    }
};
```
